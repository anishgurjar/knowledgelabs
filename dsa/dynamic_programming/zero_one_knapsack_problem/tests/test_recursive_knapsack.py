from zero_one_knapsack_problem.recursive_knapsack import knapsack_01
from zero_one_knapsack_problem.top_down_memoized import knapsack_01_memoized
from zero_one_knapsack_problem.tabulation import knapsack_01_tabulation

import pytest 

KNAPSACK_CASES = [
        # Basic: best answer takes items with weights 2 and 3
        ([1, 2, 3], [6, 10, 12], 5, 22),

        # Capacity forces you to choose 2 + 3, not weight 5 alone
        ([2, 3, 4, 5], [3, 4, 5, 6], 5, 7),

        # Larger capacity, best is weight 3 + 5
        ([2, 3, 4, 5], [3, 4, 5, 6], 8, 10),

        # Single item fits exactly
        ([5], [10], 5, 10),

        # Single item does not fit
        ([5], [10], 4, 0),

        # No items
        ([], [], 10, 0),

        # Zero capacity
        ([1, 2, 3], [10, 20, 30], 0, 0),

        # Same weights, different values: should pick highest value item
        ([4, 4, 4], [10, 20, 30], 4, 30),

        # Must choose two smaller items instead of one bigger item
        ([3, 2, 2], [5, 3, 3], 4, 6),

        # Nothing fits
        ([6, 7, 8], [10, 13, 15], 5, 0),

        # Classic recurrence test
        ([1, 3, 4, 5], [1, 4, 5, 7], 7, 9),

        # Duplicate items: 0/1 means each item can be used once
        ([2, 2, 2], [5, 5, 5], 4, 10),

        # Duplicate weights and values, best uses two weight-2 items
        ([1, 2, 2, 3], [2, 4, 4, 5], 4, 8),

        # Famous textbook case
        ([10, 20, 30], [60, 100, 120], 50, 220),

        # Non-obvious: best is weights 3 + 5, not 4 alone
        ([3, 4, 6, 5], [2, 3, 1, 4], 8, 6),
    ]

@pytest.mark.parametrize(
    "weights, values, capacity, expected",KNAPSACK_CASES
)
def test_recursive_knapsack(weights, values, capacity, expected):
    assert knapsack_01(weights, values, capacity) == expected

@pytest.mark.parametrize(
    "weights, values, capacity, expected",KNAPSACK_CASES
)
def test_memoized_knapsack(weights, values, capacity, expected):
    assert knapsack_01_memoized(weights, values, capacity) == expected

@pytest.mark.parametrize(
    "weights, values, capacity, expected",KNAPSACK_CASES
)
def test_tabulation_knapsack(weights, values, capacity, expected):
    assert knapsack_01_tabulation(weights, values, capacity) == expected
