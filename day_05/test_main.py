import pytest
from day_05 import parseContainers, doMove9000, doMove9001


@pytest.mark.parametrize("text, expected", [
    (open("day_05/case/0.txt").read(), [['Z', 'N'], ['M', 'C', 'D'], ['P']]),
    (open("day_05/case/1.txt").read(), [[], ['M', 'C'], ['P', 'D', 'N', 'Z'], ['J']])
])
def test_parsingContainers(text, expected):
    print(f"\"{text}\"")
    print(f"{expected}")
    assert parseContainers(text) == expected


@pytest.mark.parametrize("start, move, expected", [
    ([['Z', 'N'], ['M', 'C', 'D'], ['P']], "move 2 from 2 to 3", [['Z', 'N'], ['M'], ['P', 'D', 'C']]),
])
def test_CrateMover_9000(start, move, expected):
    assert doMove9000(start, move) == expected


@pytest.mark.parametrize("start, move, expected", [
    ([['Z', 'N'], ['M', 'C', 'D'], ['P']], "move 2 from 2 to 3", [['Z', 'N'], ['M'], ['P', 'C', 'D']]),
    ([['Z', 'N'], ['M', 'C', 'D'], ['P']], "move 4 from 2 to 3", [['Z', 'N'], [], ['P', 'M', 'C', 'D']]),

])
def test_CrateMover_9001(start, move, expected):
    assert doMove9001(start, move) == expected
