def buildDict(text):
    result = {}
    pwd = ["/"]
    active = result
    lines = [line.split(" ") for line in text.splitlines()]
    index = 0
    while index < len(lines):
        args = lines[index]
        if args[0] == "$":
            command = args[1]
            param = args[2:]
            if command == "cd":
                if param == ["/"]:
                    pwd = ["/"]
                    active = result
                elif param == [".."]:
                    pwd.pop()
                    if pwd == []:
                        pwd = ["/"]
                    active = result
                    for dir in pwd[1:]:
                        active = active[dir]
                else:
                    pwd += param
                    active[param[0]] = {}
                    active = active[param[0]]
            elif command == "ls":
                while index+1 < len(lines) and "$" not in lines[index+1]:

                    size, name = lines[index+1]
                    if size != "dir":
                        active[name] = int(size)
                    index += 1
        index += 1
    return {"/": result}


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
    part1 = 0
    part2 = 0
    with open("day_7/input.txt") as file:
        text = file.read()
        filesystem = buildDict(text)
        sizes = sizeup(filesystem)
        filtered = filter(lambda x: x <= 100000, sizes.values())
        part1 = sum(filtered)
        print(f"Part1: {part1}")
