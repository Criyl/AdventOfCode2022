import pytest
from day_07 import buildDict, sumDirectory, sizeup


@pytest.mark.parametrize("text, expected", [
    (
        open("day_07/case/0.txt").read(),
        {
            "/": {
                "b.txt": 14848514,
                "c.dat": 8504156,
                "a": {
                    "f": 29116,
                    "g": 2557,
                    "h.lst": 62596,
                    "e": {
                        "i": 584
                    },
                },
                "d": {
                    "j": 4060174,
                    "d.log": 8033020,
                    "d.ext": 5626152,
                    "k": 7214296
                }
            }
        }
    ),
])
def test_build_dictionary(text, expected):
    assert buildDict(text) == expected


@pytest.mark.parametrize("dir_dict, expected", [
    (
        {
            "/": {
                "b.txt": 14848514,
                "c.dat": 8504156,
                "a": {
                    "f": 29116,
                    "g": 2557,
                    "h.lst": 62596,
                    "e": {
                        "i": 584
                    },
                },
                "d": {
                    "j": 4060174,
                    "d.log": 8033020,
                    "d.ext": 5626152,
                    "k": 7214296
                }
            }
        }, 48381165
    ),
    ({"i": 584}, 584),
    ({"f": 29116, "g": 2557, "h.lst": 62596, "e": {"i": 584}}, 94853),
    ({"j": 4060174, "d.log": 8033020, "d.ext": 5626152, "k": 7214296}, 24933642)
])
def test_sum_directory(dir_dict, expected):
    assert sumDirectory(dir_dict) == expected


@pytest.mark.parametrize("directory, expected", [
    (
        {
            "/": {
                "b.txt": 14848514,
                "c.dat": 8504156,
                "a": {
                    "f": 29116,
                    "g": 2557,
                    "h.lst": 62596,
                    "e": {
                        "i": 584
                    },
                },
                "d": {
                    "j": 4060174,
                    "d.log": 8033020,
                    "d.ext": 5626152,
                    "k": 7214296
                }
            }
        },
        {
            "./": 48381165,
            "./.a": 94853,
            "./.a.e": 584,
            "./.d": 24933642
        }
    )
])
def test_sizeup(directory, expected):
    assert sizeup(directory) == expected
