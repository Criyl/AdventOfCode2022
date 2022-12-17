from typing import Callable
import re
from collections.abc import Iterable
import math


lcm = 1


class Monkey():
    monkeyID: int
    inventory: list
    _operation: Callable[[int], int]
    _check: Callable[[int], bool]
    _trueMonkey: int
    _falseMonkey: int
    inspected: int = 0
    divideBy: int = 3

    def __init__(self, monkeyID, initialInventory, operation, check, trueMonkey, falseMonkey):
        self.monkeyID = monkeyID
        self.inventory = initialInventory
        self._operation = operation
        self._check = check
        self._trueMonkey = trueMonkey
        self._falseMonkey = falseMonkey

    def throw(self, item, monkey):
        self.inspected += 1
        newValue = int(self._operation(item)/self.divideBy)
        monkey.inventory.append(newValue)
        self.inventory.remove(item)

    def turn(self, monkeys):
        while len(self.inventory) > 0:
            item = self.inventory[0]
            newValue = int(self._operation(item)/self.divideBy)
            target = self._trueMonkey if (self._check(newValue)) else self._falseMonkey
            self.throw(item, monkeys[target])

    def __str__(self):
        return str(self.inventory)

    def create(text, withLCM=False):
        lines = text.splitlines()

        monkeyID = re.match(r"Monkey (\d+):", lines[0]).groups()[0]

        inventory = re.match(r"  Starting items: ([0-9, ]+)", lines[1]).groups()[0]
        inventory = list(
                map(
                    lambda x: int(x),
                    inventory.split(', ')
                )
            )

        groups = re.match(r"  Operation: new = (old|\d+) ([+*]) (old|\d+)", lines[2]).groups()

        def doOperation(old):
            first = old if (groups[0] == "old") else int(groups[0])
            second = old if (groups[2] == "old") else int(groups[2])
            new = 0
            if groups[1] == "*":
                new = first*second
            elif groups[1] == "+":
                new = first+second
            if withLCM:
                new = new % lcm
            return new

        divisible = re.match(r"  Test: divisible by (\d+)", lines[3]).groups()[0]

        global lcm
        lcm = math.lcm(lcm, int(divisible))

        def doTest(value):
            return value % int(divisible) == 0

        trueMonkey = re.match(r"    If true: throw to monkey (\d+)", lines[4]).groups()[0]
        falseMonkey = re.match(r"    If false: throw to monkey (\d+)", lines[5]).groups()[0]

        return Monkey(int(monkeyID), inventory, doOperation, doTest, int(trueMonkey), int(falseMonkey))


if __name__ == "__main__":
    with open("day_11/input.txt") as file:
        text = file.read()

        def run(iterations, divideBy):
            monkeys = []
            for quip in text.split('\n\n'):
                monkey = Monkey.create(quip, withLCM=True)
                monkey.divideBy = divideBy
                monkeys.append(monkey)
            for _ in range(iterations):
                for monkey in monkeys:
                    monkey.turn(monkeys)

            inspected = list(map(lambda x: x.inspected, monkeys))
            inspected.sort(reverse=True)
            print(inspected[0]*inspected[1])

        run(20, 3)
        run(10_000, 1)
