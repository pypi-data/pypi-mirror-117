import re

import pytest


def exact_match(full_string):
    return f"^{re.escape(full_string)}$"


def null_action(result):
    async def action():  # pragma: no cover
        return result

    return action


def test_registry(registry):
    assert registry


def test_deleted(target):
    assert target.deleted("path/to/file")


def test_add_target_with_non_added_parent(registry):
    testing_registry = registry.Registry()
    with pytest.raises(
        ValueError,
        match=exact_match(
            "Cannot add target 'test_target' with parent action 'action'."
            " Parent action 'action' has not been added to the registry."
        ),
    ):
        testing_registry.require(
            registry.ActionOutput("action", "test_target")
        )


def test_add_deleted_with_non_added_parent(registry, target):
    testing_registry = registry.Registry()
    target = target.deleted("path/to/file")
    with pytest.raises(
        ValueError,
        match=exact_match(
            "Cannot add target Deleted(path='path/to/file') with parent "
            "action 'action'."
            " Parent action 'action' has not been added to the registry."
        ),
    ):
        testing_registry.require(registry.ActionOutput("action", target))


def test_add_target_with_different_parent(registry):
    action = null_action(None)
    testing_registry = (
        registry.Registry()
        .require(registry.ActionName(action, "null"))
        .require(registry.ActionOutput("null", "test_target"))
    )
    with pytest.raises(
        ValueError,
        match=exact_match(
            "Cannot add target 'test_target' with parent action 'action'."
            " Target 'test_target' already has parent action 'null'."
        ),
    ):
        testing_registry.require(
            registry.ActionOutput("action", "test_target")
        )


def test_name_target(registry):
    testing_registry = registry.Registry()
    with pytest.raises(
        ValueError,
        match=exact_match(
            "Cannot name target 'test_target' 'test_target'."
            " Target 'test_target' has not been added to the registry."
        ),
    ):
        testing_registry.require(
            registry.TargetName("test_target", "test_target")
        )


# Does this make sense?
def test_skip_non_existent_target(registry):
    testing_registry = registry.Registry()
    with pytest.raises(
        ValueError,
        match=exact_match(
            "Cannot skip name 'test_target'."
            " Name 'test_target' has not been assigned to any target."
        ),
    ):
        testing_registry.require(registry.SkippedName("test_target"))


def test_add_deleted_via_api(api):
    for requirement in api.target(api.deleted("path"), "parent"):
        assert requirement


def test_add_action_twice(registry):
    action = null_action(None)
    testing_registry = registry.Registry().require(
        registry.ActionName(action, "null")
    )
    assert testing_registry == testing_registry.require(
        registry.ActionName(action, "null")
    )


def test_duplicate_name_errors(registry):
    testing_registry = registry.Registry().require(
        registry.ActionName(null_action(None), "null")
    )
    action = null_action(None)
    with pytest.raises(
        ValueError,
        match=exact_match(
            "Cannot add action with name 'null'."
            " Action name 'null' has been assigned to a different action."
        ),
    ):
        testing_registry.require(registry.ActionName(action, "null"))


def test_add_input_out_of_order(registry):
    testing_registry = registry.Registry()
    with pytest.raises(
        ValueError,
        match=exact_match(
            "Cannot add target 'test_input' as an input to action"
            " 'test_action'. Action 'test_action' has not been added to the"
            " registry."
        ),
    ):
        testing_registry.require(
            registry.ActionInput("test_action", "test_input")
        )


def test_add_to_wrong_child(registry):
    testing_registry = (
        registry.Registry()
        .require(registry.ActionName(null_action(None), "test_action"))
        .require(registry.ActionName(null_action(None), "blocking_action"))
        .require(registry.ActionOutput("blocking_action", "test_input"))
    )
    with pytest.raises(
        ValueError,
        match=exact_match(
            "Cannot add target 'test_input' as an input to action"
            " 'test_action'. The most recently added action is"
            " 'blocking_action'."
        ),
    ):
        testing_registry.require(
            registry.ActionInput("test_action", "test_input")
        )


def test_add_input_not_added(registry):
    testing_registry = registry.Registry().require(
        registry.ActionName(object(), "action")
    )
    with pytest.raises(
        ValueError,
        match=exact_match(
            "Cannot add target 'test_target' as an input to action 'action'."
            " Target 'test_target' has not been added to the registry."
        ),
    ):
        testing_registry.require(registry.ActionInput("action", "test_target"))


def test_add_cycle(registry):
    testing_registry = (
        registry.Registry()
        .require(registry.ActionName(object(), "action"))
        .require(registry.ActionOutput("action", "target"))
    )
    with pytest.raises(
        ValueError,
        match=exact_match(
            "Cannot add target 'target' as an input to action 'action'."
            " The parent action of target 'target' is 'action'."
        ),
    ):
        testing_registry.require(registry.ActionInput("action", "target"))


def test_add_twice(registry):
    requirements = [
        registry.ActionName(object(), "action1"),
        registry.ActionOutput("action1", "target"),
        registry.ActionName(object(), "action2"),
        registry.ActionInput("action2", "target"),
        registry.ActionName(object(), "action3"),
    ]
    testing_registry = registry.Registry()
    for requirement in requirements:
        testing_registry = testing_registry.require(requirement)
    for requirement in requirements:
        testing_registry = testing_registry.require(requirement)
