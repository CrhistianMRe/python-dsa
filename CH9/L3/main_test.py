import pytest
from main import backoff_delays

run_cases = [
    pytest.param(1, 5, [1, 2, 4, 8, 16]),
    pytest.param(3, 4, [3, 6, 12, 24]),
]

submit_cases = [
    pytest.param(
        2,
        8,
        [2, 4, 8, 16, 32, 64, 128, 256],
        marks=pytest.mark.submit,
    ),
    pytest.param(10, 3, [10, 20, 40], marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    ("base", "num_retries", "expected_delays"), run_cases + submit_cases
)
def test_backoff_delays(base, num_retries, expected_delays):
    print("\n---------------------------------")
    print(f"Base delay: {base}")
    print(f"Retries:    {num_retries}")
    print(f"\nExpected: {expected_delays}")
    gen = backoff_delays(base)
    result = []
    for _ in range(num_retries):
        result.append(next(gen))
    print(f"Actual:   {result}")
    assert result == expected_delays

