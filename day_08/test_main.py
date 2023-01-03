import pytest
from day_08 import gridify, visible, countGrid, scenic


@pytest.mark.parametrize(
    "text, expected",
    [
        (
            "30373\n25512\n65332\n33549\n35390\n",
            [
                ["3", "0", "3", "7", "3"],
                ["2", "5", "5", "1", "2"],
                ["6", "5", "3", "3", "2"],
                ["3", "3", "5", "4", "9"],
                ["3", "5", "3", "9", "0"]],
        )
    ],
)
def test_gridify(text, expected):
    assert gridify(text) == expected


@pytest.mark.parametrize(
    "grid, expected",
    [
        (
            [
                ["3", "0", "3", "7", "3"],
                ["2", "5", "5", "1", "2"],
                ["6", "5", "3", "3", "2"],
                ["3", "3", "5", "4", "9"],
                ["3", "5", "3", "9", "0"]
            ],
            [
                [True, True, True, True, True],
                [True, True, True, False, True],
                [True, True, False, True, True],
                [True, False, True, False, True],
                [True, True, True, True, True]
            ]
        )
    ],
)
def test_visible(grid, expected):
    vis = visible(grid)
    assert vis == expected
    assert countGrid(vis) == 21


grid = [
            ["3", "0", "3", "7", "3"],
            ["2", "5", "5", "1", "2"],
            ["6", "5", "3", "3", "2"],
            ["3", "3", "5", "4", "9"],
            ["3", "5", "3", "9", "0"]
        ]


@pytest.mark.parametrize(
    "choord, expected",
    [
        ((3, 2), 8),
        ((1, 2), 4)
    ],
)
def test_scenic(choord, expected):

    assert scenic(grid, choord) == expected
