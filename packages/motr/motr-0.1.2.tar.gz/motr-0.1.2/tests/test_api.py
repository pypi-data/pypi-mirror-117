import pathlib
import types
from unittest import mock

import pytest
import trio.testing


def make_run_process(returncode):
    async def run_process(command, check, env, stdout, stderr):
        return types.SimpleNamespace(returncode=returncode)

    return run_process


def test_import(api):
    assert api


def test_cmd(api, io):
    string = pathlib.Path("string")
    env = pathlib.Path("env")
    for requirement in api.cmd(
        ["str", io.Input(string / "in"), io.Input(string / "out").as_output()],
        "test_cmd",
        env={
            "IN": io.Input(env / "in"),
            "OUT": io.Input(env / "out").as_output(),
        },
    ):
        assert requirement


def test_mkdir(api, io):
    for requirement in api.mkdir(
        io.Input(pathlib.Path("test-path")), "test_mkdir"
    ):
        assert requirement


def test_write_bytes(api, io):
    for requirement in api.write_bytes(
        io.Input(pathlib.Path("test-path")), b"test-data", "test_write_bytes"
    ):
        assert requirement


@pytest.mark.parametrize(
    "returncode,expected", [(0, "PASSED"), (1, "FAILED"), (2, "ABORTED")]
)
@trio.testing.trio_test
async def test_inner_cmd(cmd, result, tmp_path, returncode, expected):
    test_cmd = cmd.Cmd((), allowed_codes=frozenset([1]))
    with mock.patch("trio.run_process", new=make_run_process(returncode)):
        assert result.Result[expected] is await test_cmd(tmp_path)


@trio.testing.trio_test
async def test_inner_mkdir_success(mkdir, result, tmp_path):
    test_path = tmp_path / "test-path"
    assert result.Result.PASSED is await mkdir.Mkdir(test_path)(tmp_path)


@trio.testing.trio_test
async def test_inner_mkdir_failure(mkdir, result, tmp_path):
    test_path = tmp_path / "test-path"
    test_path.touch()
    assert result.Result.ABORTED is await mkdir.Mkdir(test_path)(tmp_path)


@trio.testing.trio_test
async def test_inner_write_bytes_success(write_bytes, result, tmp_path):
    test_path = tmp_path / "test-path"
    assert result.Result.PASSED is await write_bytes.WriteBytes(
        test_path, b""
    )(tmp_path)


@trio.testing.trio_test
async def test_inner_write_bytes_failure(write_bytes, result, tmp_path):
    test_path = tmp_path / "test-path"
    test_path.mkdir()
    assert result.Result.ABORTED is await write_bytes.WriteBytes(
        test_path, b""
    )(tmp_path)
