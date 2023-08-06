import pathlib
import re
import sys

import attr
import trio
import wheel_filename

from motr import api
from motr._api.actions import cmd as cmd_
from motr._api.actions import io
from motr._api.requirements import action
from motr._api.requirements import target
from motr.core import result as result_


REQUIREMENTS_FILE = io.Input(pathlib.Path(".motr/requirements.txt"))


@attr.dataclass(frozen=True)
class Venv:
    root: pathlib.Path
    name: str

    @property
    def action_name(self):
        return f"{self.root}-{self.name}"

    @property
    def create_name(self):
        return f"make-venv-{self.action_name}"

    @property
    def update_name(self):
        return f"update-pip-{self.action_name}"

    @property
    def install_name(self):
        return f"install-requirements-{self.action_name}"

    @property
    def root_path(self):
        return self.root / self.name

    @property
    def bin_dir(self):
        return self.root_path / "bin"

    @property
    def pip(self):
        return io.Input(self.bin_dir / "pip")

    def create(self):
        yield from api.cmd(
            [sys.executable, "-m", "venv", "--clear", self.root_path],
            self.create_name,
        )
        yield from target.target(self.bin_dir, self.create_name)

    def update(self):
        yield from api.cmd(
            [self.pip.as_output(), "install", "-U", "pip"],
            self.update_name,
            self.bin_dir,
        )

    def install(self, *pip_args):
        yield from api.cmd((self.pip, "install") + pip_args, self.install_name)

    def command(self, command):
        command_path = self.bin_dir / command
        yield from target.target(command_path, self.install_name)
        return io.Input(command_path)


dot_dir = pathlib.Path(".motr")
requirements_dir = pathlib.Path("requirements")
reports_dir = pathlib.Path("reports")


def setup_venv(name, command, *pip_args):
    venv = Venv(dot_dir, name)

    yield from venv.create()
    yield from venv.update()
    yield from venv.install(*pip_args)

    return (yield from venv.command(command))


@attr.dataclass(frozen=True)
class FlitToRequirements:
    flit: io.Input
    outfile: io.Input

    async def __call__(self, log_dir):
        nested = log_dir / "nested"
        await trio.Path(nested).mkdir()
        result = await cmd_.Cmd(
            (
                str(self.flit.path), "build", "--format", "wheel",
            ),
        )(nested)
        if result is not result_.Result.PASSED:
            return result_.Result.ABORTED
        # It should be safe to read the log file in *text* mode.
        build_log = await trio.Path(nested / "err.txt").read_text()
        wheel_re = r"Built wheel:\s*(\S*)"
        build_match = re.search(wheel_re, build_log)
        if build_match is None:
            return result_.Result.ABORTED
        build_path = pathlib.Path(build_match.group(1))
        package_name = wheel_filename.parse_wheel_filename(build_path).project
        await trio.Path(self.outfile.path).write_text(
            f"{package_name} @ {build_path.resolve().as_uri()}\n"
        )
        return result_.Result.PASSED


def flit(outfile):
    flit_cmd = yield from setup_venv("flit", "flit", "flit")
    flit_to_requirements = FlitToRequirements(flit_cmd, outfile)
    action_name = "flit-build"
    yield from action.action(flit_to_requirements, action_name, flit_cmd.path)
    yield from target.target(outfile.path, action_name)
    return outfile


def venv_wrapper(name, command, requirements_file, *pip_args):
    return (
        yield from setup_venv(
            name,
            command,
            "-r",
            (requirements_dir / requirements_file).with_suffix(".txt"),
            *pip_args,
        )
    )


def pytest_suffix(junit_file):
    return (
        "tests",
        "-p",
        "no:cacheprovider",
        "--junitxml",
        junit_file.as_output(),
    )


def run_pytest(
    env_name, requirement_name, runner, report_name, test_extra_inputs=()
):
    command_name = runner[0]
    requirements_file = yield from flit(REQUIREMENTS_FILE)
    command = yield from venv_wrapper(
        env_name, command_name, requirement_name, "-r", requirements_file
    )
    runner = (command,) + runner[1:]
    report_dir = io.Input(reports_dir / report_name)
    yield from api.mkdir(report_dir, f"mkdir-{report_name}")
    junit_file = io.Input(report_dir.path / "junit.xml")
    yield from (
        api.cmd(
            runner + pytest_suffix(junit_file),
            f"pytest-{env_name}",
            report_dir.path,
            *test_extra_inputs,
            allowed_codes=[1],
        )
    )
    junit2html = yield from venv_wrapper(
        "junit-report", "junit2html", "junit-report"
    )
    html_file = io.Input(report_dir.path / "index.html")
    yield from (
        api.cmd(
            [
                junit2html,
                junit_file,
                html_file.as_output(env_name),
            ],
            f"pytest-{env_name}-report",
        )
    )


def changes():
    flake8_report_dir = io.Input(reports_dir / "flake8")
    flake8_report_file = flake8_report_dir.path / "index.html"
    flake8 = yield from venv_wrapper("check", "flake8", "check")
    yield from api.mkdir(flake8_report_dir, "mkdir-flake8")
    yield from api.cmd(
        [
            flake8,
            "--format=html",
            "--htmldir",
            flake8_report_dir,
            "--isort-show-traceback",
            "src",
            "tests",
        ],
        "check",
        allowed_codes=[1],
    )
    yield from target.target(flake8_report_file, "check", "check")

    requirements_file = yield from flit(REQUIREMENTS_FILE)

    mypy_report_dir = reports_dir / "mypy"
    mypy_report_file = io.Input(mypy_report_dir / "junit.xml")
    mypy_coverage_dir = io.Input(reports_dir / "mypy-coverage")
    mypy_coverage_file = mypy_coverage_dir.path / "index.html"
    mypy = yield from venv_wrapper("mypy", "mypy", "mypy", "-r", requirements_file)
    yield from api.mkdir(io.Input(mypy_report_dir), "mkdir-mypy-report")
    yield from api.mkdir(mypy_coverage_dir, "mkdir-mypy-coverage")
    yield from api.cmd(
        [
            mypy,
            "--html-report",
            mypy_coverage_dir,
            "--junit-xml",
            mypy_report_file.as_output(),
            "src",
        ],
        "mypy",
        mypy_report_dir,
        allowed_codes=[1],
    )
    yield from target.target(mypy_coverage_file, "mypy", "mypy")
    junit2html = yield from venv_wrapper(
        "junit-report", "junit2html", "junit-report"
    )
    mypy_report_html = io.Input(mypy_report_dir / "index.html")
    yield from api.cmd(
        [junit2html, mypy_report_file, mypy_report_html.as_output("mypy")],
        "mypy-report",
    )

    yield from run_pytest(
        "nocov", "pytest", ("python", "-m", "pytest"), "pytest"
    )

    coverage = yield from venv_wrapper("coverage", "coverage", "coverage")
    coverage_deleted = api.deleted(pathlib.Path(".coverage"))
    yield from api.cmd([coverage, "erase"], "coverage-erase")
    yield from target.target(coverage_deleted, "coverage-erase")
    initial_coverage = "initial-coverage"
    updated_coverage_file = pathlib.Path(".coverage")
    yield from run_pytest(
        "cover",
        "cover",
        ("coverage", "run", "-m", "pytest"),
        "pytest-cover",
        (coverage_deleted,),
    )
    yield from target.target(initial_coverage, "pytest-cover")
    yield from api.cmd(
        [coverage, "combine"],
        "coverage-combine",
        initial_coverage,
    )
    yield from target.target(updated_coverage_file, "coverage-combine")
    yield from api.cmd(
        [
            coverage,
            "html",
            "--show-contexts",
            "-d",
            io.Input(reports_dir / "coverage").as_output("cover"),
        ],
        "coverage-html",
        updated_coverage_file,
    )
    yield from api.cmd(
        [
            coverage,
            "report",
            "--skip-covered",
            "-m",
            "--fail-under=100",
        ],
        "coverage-report",
        updated_coverage_file,
        allowed_codes=[2],
    )

    yield from target.target("coverage-report", "coverage-report", "cover")

    profile_dir = io.Input(reports_dir / "profile")

    yield from api.mkdir(profile_dir, "mkdir-profile")
    yield from run_pytest(
        "profile",
        "profile",
        (
            "pyinstrument",
            "--renderer",
            "html",
            "--outfile",
            io.Input(profile_dir.path / "index.html").as_output("profile"),
            "-m",
            "pytest",
        ),
        "pytest-profile",
        (profile_dir.path,),
    )


MOTR_CONFIG = api.build(changes())
