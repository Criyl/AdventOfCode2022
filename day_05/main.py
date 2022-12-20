import re
import copy


def parseContainers(containers):
    stacks = []

    grid = [list(line) for line in containers.splitlines()]

    height = len(grid)-1
    indexLine = grid[height]
    for i, v in enumerate(indexLine):
        if v == ' ':
            continue
        stack = []
        for j in reversed(range(0, height)):
            if i < len(grid[j]):
                crate = grid[j][i]
                if crate != ' ':
                    stack.append(crate)
        stacks.append(stack)

    return stacks


def doMove9000(stacks, move):
    result = stacks.copy()
    pattern = r"move (\d+) from (\d+) to (\d+)"
    groups = re.match(pattern, move).groups()

    quantity = int(groups[0])
    start = int(groups[1])
    end = int(groups[2])

    for _ in range(0, quantity):
        popped = stacks[start-1].pop()
        stacks[end-1].append(popped)

    return result


def doMove9001(stacks, move):
    result = stacks.copy()
    pattern = r"move (\d+) from (\d+) to (\d+)"
    groups = re.match(pattern, move).groups()

    quantity = int(groups[0])
    start = int(groups[1])
    end = int(groups[2])

    tertiary_stack = []
    for _ in range(0, quantity):
        stack = stacks[start-1]
        if len(stack) == 0:
            break
        popped = stack.pop()
        tertiary_stack.append(popped)

    for _ in range(0, len(tertiary_stack)):
        popped = tertiary_stack.pop()
        stacks[end-1].append(popped)

    return result


if __name__ == "__main__":
    part1_containers = ""
    part2_containers = ""
    with open("day_05/input.txt") as file:
        crateString = ""
        line = file.readline()
        while line != "\n":
            crateString += line
            line = file.readline()
        containers = parseContainers(crateString)

        part1_containers = copy.deepcopy(containers)
        part2_containers = copy.deepcopy(containers)

        for line in file.readlines():
            part1_containers = doMove9000(part1_containers, line)
            part2_containers = doMove9001(part2_containers, line)

    tops = [stack[len(stack)-1] for stack in part1_containers]
    print("".join(tops))

    tops = [stack[len(stack)-1] for stack in part2_containers]
    print("".join(tops))
