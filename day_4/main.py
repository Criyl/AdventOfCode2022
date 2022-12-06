
def isRedundant(range_a, range_b):
    set_a = set(range_a)
    set_b = set(range_b)
    return set_a.issubset(set_b) or set_b.issubset(set_a)


def stringToRange(rangeString):
    split = rangeString.split('-')
    return range(int(split[0]), int(split[1])+1)


count = 0
with open("input.txt") as file:
    for line in file.readlines():
        a, b = line.strip().split(',')

        range_a = stringToRange(a)
        range_b = stringToRange(b)

        redundant = isRedundant(range_a, range_b)
        count += redundant
        print(f" {a},{b} = {redundant}")
print(count)
