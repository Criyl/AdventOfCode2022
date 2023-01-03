import pytest
from day_12 import solve


@pytest.mark.parametrize(
    "prompt, expected",
    [
        (
            "Sabqponm\nabcryxxl\naccszExk\nacctuvwj\nabdefghi",
            32
        )
    ]
)
def test_solve(prompt, expected):
    assert len(solve(prompt)) == expected


@pytest.mark.parametrize(
    "prompt, expected",
    [
        (
            "Sabqponm\nabcryxxl\naccszExk\nacctuvwj\nabdefghi",
            30
        )
    ]
)
def test_solve_part2(prompt, expected):
    assert len(solve(prompt, startOnly=False)) == expected
