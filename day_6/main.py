
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
    with open("day_6/input.txt") as file:
        line = file.readline()
        print(line)
        print(getMarker(line))
