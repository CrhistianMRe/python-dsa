import pytest

from main import is_balanced

run_cases = [
    ("(", False),
    ("()", True),
    ("(())", True),
]

submit_cases = [
    pytest.param("()()", True, marks=pytest.mark.submit),
    pytest.param("(()))", False, marks=pytest.mark.submit),
    pytest.param("((())())", True, marks=pytest.mark.submit),
    pytest.param("(()(()", False, marks=pytest.mark.submit),
    pytest.param(")(", False, marks=pytest.mark.submit),
    pytest.param(")()(()", False, marks=pytest.mark.submit),
    pytest.param("())(()", False, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(("input1", "expected_output"), run_cases + submit_cases)
def test_is_balanced(input1, expected_output):
    print("\n---------------------------------")
    print(f"Input: {input1}")
    print(f"Expected: {expected_output}")
    result = is_balanced(input1)
    print(f"Actual:   {result}")
    assert result == expected_output

