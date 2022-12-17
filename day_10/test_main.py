import pytest

from day_10 import process, crtRow


@pytest.mark.parametrize(
    "content, expected",
    [
        ('noop\naddx 3\naddx -5', [1, 1, 1, 4, 4, -1]),
    ]
)
def test_process(content, expected):
    assert process(content) == expected


@pytest.mark.parametrize(
    "cycles, expected",
    [
        (
            [1, 1, 16, 16, 5, 5, 11, 11, 8, 8, 13, 13, 12, 12, 4, 4, 17, 17, 21, 21, 21, 20],
            '##..##..##..##..##..##'
        ),
    ]
)
def test_crtRow(cycles, expected):
    assert crtRow(cycles) == expected
