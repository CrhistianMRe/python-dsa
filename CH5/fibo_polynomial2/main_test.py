import pytest

from main import fib

run_cases = [
    (1, 1),
    (10, 55),
    (20, 6765),
]

submit_cases = [
    pytest.param(0, 0, marks=pytest.mark.submit),
    pytest.param(40, 102334155, marks=pytest.mark.submit),
    pytest.param(70, 190392490709135, marks=pytest.mark.submit),
    pytest.param(
        160,
        1226132595394188293000174702095995,
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(("input1", "expected_output"), run_cases + submit_cases)
def test_fib(input1, expected_output):
    print("\n---------------------------------")
    print(f"Input: {input1}")
    print(f"Expected:  {expected_output}")
    result = fib(input1)
    print(f"Actual: {result}")
    assert result == expected_output

