import pytest
from main import isRedundant

@pytest.mark.parametrize("range_a, range_b, expected", [
    (range(2, 4+1), range(6, 8+1), False),
    (range(2, 3+1), range(4, 5+1), False),
    (range(5, 7+1), range(7, 9+1), False),
    (range(2, 8+1), range(3, 7+1), True),
    (range(6, 6+1), range(4, 6+1), True),
    (range(2, 6+1), range(4, 8+1), False)
])
def test_redundant(range_a, range_b, expected):
    assert isRedundant(range_a, range_b) == expected
