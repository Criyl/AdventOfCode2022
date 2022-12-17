import pytest
from day_11 import Monkey


@pytest.mark.parametrize(
    "text, monkeyID, inventory, operation, test, trueMonkey, falseMonkey",
    [
        (
            'Monkey 0:\n  Starting items: 79, 98\n  Operation: new = old * 19\n  Test: divisible by 23\n    If true: throw to monkey 2\n    If false: throw to monkey 3',  # noqa: E501
            0,
            [79, 98],
            lambda old: old * 19,
            lambda num: num % 23 == 0,
            2, 3
        ),
        (
            'Monkey 1:\n  Starting items: 54, 65, 75, 74\n  Operation: new = old + 6\n  Test: divisible by 19\n    If true: throw to monkey 2\n    If false: throw to monkey 0',  # noqa: E501
            1,
            [54, 65, 75, 74],
            lambda old: old + 6,
            lambda num: num % 19 == 0,
            2, 0
        ),
        (
            'Monkey 2:\n  Starting items: 79, 60, 97\n  Operation: new = old * old\n  Test: divisible by 13\n    If true: throw to monkey 1\n    If false: throw to monkey 3',  # noqa: E501
            2,
            [79, 60, 97],
            lambda old: old * old,
            lambda num: num % 13 == 0,
            1, 3
        ),
        (
            'Monkey 3:\n  Starting items: 74\n  Operation: new = old + 3\n  Test: divisible by 17\n    If true: throw to monkey 0\n    If false: throw to monkey 1',  # noqa: E501
            3,
            [74],
            lambda old: old + 3,
            lambda num: num % 17 == 0,
            0, 1
        ),


    ]
)
def test_monkey_create(text, monkeyID, inventory, operation, test, trueMonkey, falseMonkey):
    monkey = Monkey.create(text)
    assert monkey.monkeyID == monkeyID
    assert monkey.inventory == inventory

    for value in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
        assert monkey._operation(value) == operation(value)
        assert monkey._check(value) == test(value)

    assert monkey._trueMonkey == trueMonkey
    assert monkey._falseMonkey == falseMonkey


@pytest.mark.parametrize(
    "monkeys, expected",
    [
        (
            [
                Monkey(0, [79, 98], lambda old: old * 19, lambda num: num % 23 == 0, 2, 3),
                Monkey(1, [54, 65, 75, 74], lambda old: old + 6, lambda num: num % 19 == 0, 2, 0),
                Monkey(2, [79, 60, 97], lambda old: old * old, lambda num: num % 13 == 0, 1, 3),
                Monkey(3, [74], lambda old: old + 3, lambda num: num % 17 == 0, 0, 1)
            ],
            [
                [20, 23, 27, 26],
                [2080, 25, 167, 207, 401, 1046],
                [],
                []
            ]
        )
    ]
    )
def test_monkey_turn(monkeys, expected):
    for monkey in monkeys:
        print(f"Before{list(map(lambda x: x.inventory, monkeys))}")
        monkey.turn(monkeys)
        print(f"After{list(map(lambda x: x.inventory, monkeys))}")

    for i, monkey in enumerate(monkeys):
        assert monkey.inventory == expected[i]
