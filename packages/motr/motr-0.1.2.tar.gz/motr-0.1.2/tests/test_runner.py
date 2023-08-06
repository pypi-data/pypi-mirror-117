import contextlib
import itertools
import pathlib

import attr
import pytest
import trio


def null_action(result):
    async def action(tmpdir):
        return result

    return action


@attr.dataclass(frozen=True)
class SynchAction:
    result: object  # Filled in by test.
    before: trio.Event
    after: trio.Event

    async def __call__(self, tmpdir):
        await self.before.wait()
        self.after.set()
        return self.result


@contextlib.contextmanager
def null_report(action):
    yield


def test_import(runner):
    assert runner


def test_task_wrapper(runner):
    wrapper = runner.TaskWrapper()
    run_count = 0

    async def run():
        nonlocal run_count
        run_count += 1

    trio.run(wrapper, run)
    assert run_count == 1
    trio.run(wrapper, run)
    assert run_count == 1


@pytest.mark.parametrize("count", list(range(10)))
def test_run_all(runner, count):
    run_count = 0

    async def run(arg):
        nonlocal run_count
        run_count += 1

    trio.run(runner.run_all, run, [None] * count)
    assert run_count == count


def test_target_action_comprehensive(exc, result, runner, api, tmpdir):
    pass_result = result.Result.PASSED
    fail_result = result.Result.FAILED
    abort_result = result.Result.ABORTED
    first_action = null_action(pass_result)
    second_action = null_action(abort_result)
    third_action = null_action(pass_result)
    reg = api.build(
        itertools.chain(
            api.action(first_action, "first"),
            api.target("first_res", "first"),
            api.action(second_action, "second", "first_res"),
            api.target("second_res", "second"),
            api.action(third_action, "third", "second_res"),
            api.target("third_res", "third"),
        ),
    )
    results = {pass_result: [], fail_result: [], abort_result: []}
    target = runner.Target(reg, pathlib.Path(tmpdir), null_report, results)

    with pytest.raises(exc.MOTRTaskError):
        trio.run(target, "third_res")

    assert results == {
        pass_result: ["first"],
        fail_result: [],
        abort_result: ["second"],
    }


@pytest.mark.parametrize(
    "sequence",
    [
        (0, 0, 1, 1),
        (0, 1, 0, 1),
        (0, 1, 1, 0),
        (1, 0, 0, 1),
        (1, 0, 1, 0),
        (1, 1, 0, 0),
    ],
)
def test_implicit_sequencing(result, runner, api, sequence, tmpdir):
    event = trio.Event()
    event.set()
    sequences = [[], []]
    pass_result = result.Result.PASSED
    fail_result = result.Result.FAILED
    abort_result = result.Result.ABORTED
    final_action = null_action(pass_result)

    for index in sequence:
        new_event = trio.Event()
        sequences[index].append(SynchAction(pass_result, event, new_event))
        event = new_event

    args = []

    for index, sub_sequence in enumerate(sequences):
        action_0 = f"{index}0"
        res_0 = action_0 + "_res"
        action_1 = f"{index}1"
        res_1 = action_1 + "_res"
        args.extend(api.action(sub_sequence[0], action_0))
        args.extend(api.target(res_0, action_0))
        args.extend(api.action(sub_sequence[1], action_1, res_0))
        args.extend(api.target(res_1, action_1))

    args.extend(api.action(final_action, "final_action", "01_res", "11_res"))
    args.extend(api.target("final_res", "final_action"))
    reg = api.build(args)
    results = {pass_result: [], fail_result: [], abort_result: []}
    target = runner.Target(reg, pathlib.Path(tmpdir), null_report, results)
    trio.run(target, "final_res")

    assert results[pass_result]
    assert not results[fail_result]
    assert not results[abort_result]
