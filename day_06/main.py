
def getMarker(signal, n=4):
    sequence = []
    index = 0

    for c in signal:
        sequence.append(c)
        index += 1
        if len(sequence) > n:
            sequence = sequence[1:]
        if len(set(sequence)) == n:
            break

    return index


if __name__ == "__main__":
    part1 = ""
    part2 = ""
    with open("day_06/input.txt") as file:
        line = file.readline()
        part1 = getMarker(line)
        part2 = getMarker(line, 14)
    print(f"Part1: {part1}")
    print(f"Part2: {part2}")
