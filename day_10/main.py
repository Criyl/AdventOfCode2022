def process(content):
    cycles = [1]
    x = 1

    for line in content.splitlines():
        if line == "noop":
            cycles.append(x)
        else:
            operation = line.split(' ')[1]
            cycles.append(x)
            x = x+int(operation)
            cycles.append(x)

    return cycles


def crtRow(cycles):
    output = ""

    for i, v in enumerate(cycles):
        if abs(i-v) < 2:
            output += "#"
        else:
            output += "."

    return output


if __name__ == "__main__":
    with open("day_10/input.txt") as file:
        text = file.read()
        cycles = process(text)

        part1 = 0
        for i in [20, 60, 100, 140, 180, 220]:
            v = cycles[i-1]*(i)
            part1 += v

        print(part1)

        for i in range(0, int(len(cycles)/40)):
            print(crtRow(cycles[40*i:40*i+40]))
