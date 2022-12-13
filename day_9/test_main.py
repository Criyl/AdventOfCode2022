import pytest
from day_9 import generatePath, predict, iterate


@pytest.mark.parametrize(
    "steps, length, expected",
    [
        (
            "R 4\nU 4\nL 3\nD 1\nR 4\nD 1\nL 5\nR 2",
            10,
            #  H       1       2       3       4       5       6       7       8       9
            [(2, 2), (1, 2), (2, 2), (3, 2), (2, 2), (1, 1), (0, 0), (0, 0), (0, 0), (0, 0)]
        ),
        (
            "R 4\nU 4\nL 3\nD 1\nR 4\nD 1\nL 5\nR 2",
            2,
            [(2, 2), (1, 2)]
        )
    ],
)
def test_path(steps, length, expected):
    history = generatePath(steps, length)
    assert history[len(history)-1] == expected


@pytest.mark.parametrize(
    "head, tail, expected",
    (
        # R 4
        (((1, 0)), ((0, 0)), ((0, 0))),
        (((2, 0)), ((0, 0)), ((1, 0))),
        (((3, 0)), ((1, 0)), ((2, 0))),
        (((4, 0)), ((2, 0)), ((3, 0))),
        # U 4
        (((4, 1)), ((3, 0)), ((3, 0))),
        (((4, 2)), ((3, 0)), ((4, 1))),
        (((4, 3)), ((4, 1)), ((4, 2))),
        (((4, 4)), ((4, 2)), ((4, 3))),
        # L 3
        (((3, 4)), ((4, 3)), ((4, 3))),
        (((2, 4)), ((4, 3)), ((3, 4))),
        (((1, 4)), ((3, 4)), ((2, 4))),
        # D 1
        (((1, 3)), ((2, 4)), ((2, 4))),
        # R 4
        (((2, 3)), ((2, 4)), ((2, 4))),
        (((3, 3)), ((2, 4)), ((2, 4))),
        (((4, 3)), ((2, 4)), ((3, 3))),
        (((5, 3)), ((3, 3)), ((4, 3))),
        # D 1
        (((5, 2)), ((4, 3)), ((4, 3))),
        # L 5
        (((4, 2)), ((4, 3)), ((4, 3))),
        (((3, 2)), ((4, 3)), ((4, 3))),
        (((2, 2)), ((4, 3)), ((3, 2))),
        (((1, 2)), ((3, 2)), ((2, 2))),
        (((0, 2)), ((2, 2)), ((1, 2))),
        # R 2
        (((1, 2)), ((1, 2)), ((1, 2))),
        (((2, 2)), ((1, 2)), ((1, 2))),

        (((2, 2)), ((0, 0)), ((1, 1))),
    )
)
def test_predict(head, tail, expected):
    assert predict(head, tail) == expected


@pytest.mark.parametrize(
    "direction, rope, expected",
    [
        ('U', [(4, 1), (3, 0), (2, 0), (1, 0), (0, 0), (0, 0)], [(4, 2), (4, 1), (3, 1), (2, 1), (1, 1), (0, 0)]),
        ('U', [(4, 2), (4, 1), (3, 1), (2, 1), (1, 1), (0, 0)], [(4, 3), (4, 2), (3, 1), (2, 1), (1, 1), (0, 0)]),
        ('U', [(4, 3), (4, 2), (3, 1), (2, 1), (1, 1), (0, 0)], [(4, 4), (4, 3), (4, 2), (3, 2), (2, 2), (1, 1)]),
    ]
)
def test_iterate(direction, rope,  expected):
    assert iterate(direction, rope) == expected
