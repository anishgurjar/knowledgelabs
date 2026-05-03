from fractional_knapsack.main import main
import pytest


@pytest.mark.parametrize("values, weights, capacity, expected", [
    # basic case
    ([60, 100, 120], [10, 20, 30], 50, 240.0),

    # exact fit
    ([10, 20, 30], [1, 1, 1], 3, 60.0),

    # take fraction of last item
    ([100, 60, 120], [20, 10, 30], 25, 135.0),

    # single item, partial
    ([500], [50], 10, 100.0),

    # zero capacity
    ([10, 20, 30], [1, 1, 1], 0, 0.0),

    # items already optimal in order
    ([100, 90, 80], [10, 10, 10], 15, 145.0),

    # tricky: high value but heavy
    ([500, 30], [100, 10], 10, 50.0),

    # large capacity, take all
    ([10, 20, 30], [5, 10, 15], 100, 60.0),
])
def test_fractional_knapsack(values, weights, capacity, expected):
    result = main(values, weights, capacity)
    assert abs(result - expected) < 1e-5