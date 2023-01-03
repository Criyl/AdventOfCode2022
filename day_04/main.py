
def isRedundant(range_a, range_b):
    set_a = set(range_a)
    set_b = set(range_b)
    return set_a.issubset(set_b) or set_b.issubset(set_a)


def doOverlap(range_a, range_b):
    set_a = set(range_a)
    set_b = set(range_b)
    return len(set_a.intersection(set_b)) != 0


def stringToRange(rangeString):
    split = rangeString.split('-')
    return range(int(split[0]), int(split[1])+1)


if __name__ == "__main__":
    part1 = 0
    part2 = 0
    with open("day_04/input.txt") as file:
        for line in file.readlines():
            a, b = line.strip().split(',')

            range_a = stringToRange(a)
            range_b = stringToRange(b)

            redundant = isRedundant(range_a, range_b)
            overlap = doOverlap(range_a, range_b)
            part1 += redundant
            part2 += overlap

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
