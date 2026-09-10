import pytest
from main import BSTNode
from user import User, get_users

run_cases = [
    pytest.param(5, True),
    pytest.param(3, False),
]

submit_cases = [
    pytest.param(1, True, marks=pytest.mark.submit),
    pytest.param(21, False, marks=pytest.mark.submit),
    pytest.param(17, True, marks=pytest.mark.submit),
    pytest.param(7, True, marks=pytest.mark.submit),
]


def populate_tree(nodes):
    if not nodes:
        return None
    tree = BSTNode(nodes[0])
    for node in nodes[1:]:
        tree.insert(node)
    return tree


@pytest.mark.parametrize(("val_to_check", "expected_output"), run_cases + submit_cases)
def test_node_exists(val_to_check, expected_output):
    print("\n---------------------------------")
    users = get_users(11)
    tree = populate_tree(users)
    user_to_find = User(val_to_check)
    print("Tree nodes:")
    for user in users:
        print(f" * {user}")
    print(f"Searching for: {user_to_find}")
    result = tree.exists(user_to_find)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output

