import pytest
from day_5 import parseContainers, doMove


@pytest.mark.parametrize("text, expected", [
    (open("day_5/case/0.txt").read(), [['Z', 'N'], ['M', 'C', 'D'], ['P']]),
    (open("day_5/case/1.txt").read(), [[], ['M', 'C'], ['P', 'D', 'N', 'Z'], ['J']])
])
def test_parsingContainers(text, expected):
    print(f"\"{text}\"")
    print(f"{expected}")
    assert parseContainers(text) == expected


@pytest.mark.parametrize("start, move, expected", [
    ([['Z', 'N'], ['M', 'C', 'D'], ['P']], "move 2 from 2 to 3", [['Z', 'N'], ['M'], ['P', 'D', 'C']]),
])
def test_move(start, move, expected):
    assert doMove(start, move) == expected
