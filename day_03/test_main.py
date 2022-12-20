import pytest
from day_03 import getCommon, getScore, intersectMany


@pytest.mark.parametrize("sack, expected", [
    ('vJrwpWtwJgWrhcsFMMfFFhFp', 'p'),
    ('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'L'),
    ('PmmdzqPrVvPwwTWBwg', 'P'),
    ('wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'v'),
    ('ttgJtRGJQctTZtZT', 't'),
    ('CrZsJsPPZsGzwwsLwLmpwMDw', 's')
])
def test_common(sack, expected):
    assert getCommon(sack) == expected


@pytest.mark.parametrize("sacks, expected", [
    (['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg'], 'r'),
    (['wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw'], 'Z')
])
def test_badge(sacks, expected):
    assert intersectMany(sacks) == expected


@pytest.mark.parametrize("common, expected", [
    ('p', 16),
    ('L', 38),
    ('P', 42),
    ('v', 22),
    ('t', 20),
    ('s', 19)
])
def test_score(common, expected):
    assert getScore(common) == expected
