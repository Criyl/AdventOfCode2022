import re


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


def doMove(stacks, move):
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


if __name__ == "__main__":

    with open("day_5/input.txt") as file:
        crateString = ""
        line = file.readline()
        while line != "\n":
            crateString += line
            line = file.readline()

        containers = parseContainers(crateString)
        
        for line in file.readlines():
            containers = doMove(containers, line)
            
        print(containers)
    tops = [stack[len(stack)-1] for stack in containers]
    print("".join(tops))
