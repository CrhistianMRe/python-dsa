import pytest
from main import BSTNode
from user import get_users

run_cases = [
    pytest.param(2, 2),
    pytest.param(6, 3),
]

submit_cases = [
    pytest.param(0, 0, marks=pytest.mark.submit),
    pytest.param(1, 1, marks=pytest.mark.submit),
    pytest.param(16, 7, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(("num_users", "expected_output"), run_cases + submit_cases)
def test_height(num_users, expected_output):
    users = get_users(num_users)
    if not users:
        root = BSTNode()
    else:
        root = BSTNode(users[0])
        for user in users[1:]:
            root.insert(user)

    print("\n---------------------------------")
    print(f"Users: {[str(user) for user in users]}")
    print_tree(root)
    print(f"Expecting height: {expected_output}")
    result = root.height()
    print(f"Actual height: {result}")
    assert result == expected_output


def print_tree(bst_node):
    lines = []
    format_tree_string(bst_node, lines)
    print("\n".join(lines))


def format_tree_string(bst_node, lines, level=0):
    if bst_node is not None:
        format_tree_string(bst_node.right, lines, level + 1)
        lines.append(" " * 4 * level + "> " + str(bst_node.val))
        format_tree_string(bst_node.left, lines, level + 1)

