def handleChangeDirectory(param, head, working_directory, active):
    if param == ["/"]:
        working_directory = ["/"]
        active = head
    elif param == [".."]:
        working_directory.pop()
        if working_directory == []:
            working_directory = ["/"]
        active = head
        for dir in working_directory[1:]:
            active = active[dir]
    else:
        working_directory += param
        active[param[0]] = {}
        active = active[param[0]]
    return (working_directory, active)


def buildDict(text):
    head = {}
    working_directory = ["/"]
    active = head
    lines = [line.split(" ") for line in text.splitlines()]
    index = 0
    while index < len(lines):
        args = lines[index]
        if args[0] == "$":
            command = args[1]
            param = args[2:]
            if command == "cd":
                working_directory, active = handleChangeDirectory(param, head, working_directory, active)
            elif command == "ls":
                while index+1 < len(lines) and "$" not in lines[index+1]:
                    size, name = lines[index+1]
                    if size != "dir":
                        active[name] = int(size)
                    index += 1
        index += 1
    return {"/": head}


def sumDirectory(directory):
    sum = 0
    for sub in directory:
        entry = directory[sub]
        if isinstance(entry, int):
            sum += entry
        else:
            subSum = sumDirectory(entry)
            sum += subSum
    return sum


def sizeup(directory, name=""):
    runningSum = 0
    entries = {}

    for key, value in directory.items():
        if isinstance(value, int):
            runningSum += value
        else:
            subEntries = sizeup(value, name=f"{name}.{key}")
            entries.update(subEntries)
            subSum = sumDirectory(value)
            entries[f"{name}.{key}"] = subSum
            runningSum += subSum
    return entries


if __name__ == "__main__":
    with open("day_07/input.txt") as file:
        text = file.read()
        filesystem = buildDict(text)
        sizes = sizeup(filesystem)
        filtered = filter(lambda x: x <= 100000, sizes.values())
        part1 = sum(filtered)
        print(f"Part1: {part1}")

        desired_space = sizes['./'] - 40000000
        filtered = filter(lambda x: x >= desired_space, sizes.values())
        sorted_sizes = sorted(filtered)
        part2 = sorted_sizes[0]
        print(f"Part2: {part2}")
