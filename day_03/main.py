
def getCommon(sack: str) -> str:
    half = int(len(sack)/2)
    compartments = [sack[:half], sack[half:]]
    return intersectMany(compartments)


def getScore(common):
    ordinal = ord(common)
    if ordinal >= 97:
        return ordinal - 96
    return ordinal - 64 + 26


def intersectMany(sacks):
    intersect = set(sacks[0])
    for sack in sacks[1:]:
        intersect = intersect.intersection(set(sack))
    return "".join(intersect)


if __name__ == "__main__":
    part1 = 0

    thruple = []
    part2 = 0

    with open("day_03/input.txt") as file:
        for line in file.readlines():
            stripped = line.strip()

            half = int(len(stripped)/2)
            compartments = [stripped[:half], stripped[half:]]
            common = intersectMany(compartments)

            part1 += getScore(common)

            thruple += [stripped]
            if len(thruple) == 3:
                badge = intersectMany(thruple)
                part2 += getScore(badge)
                thruple = []

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
