
def getCommon(sack: str):
    half = int(len(sack)/2)
    first = sack[:half]
    second = sack[half:]
    return "".join(set(first).intersection(second))


def getScore(common):
    ordinal = ord(common)
    if ordinal >= 97:
        return ordinal - 96
    return ordinal - 64 + 26


total_score = 0
with open("input.txt") as file:
    for line in file.readlines():
        stripped = line.strip()
        print(stripped)
        common = getCommon(stripped)
        score = getScore(common)
        total_score += score
print(total_score)