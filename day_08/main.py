import numpy as np


def gridify(text):
    return [list(lineA) for lineA in text.splitlines()]


def calculateVisibility(grid, choord):
    x, y = choord
    top = grid[x][y]

    down = True
    for i in range(x+1, len(grid)):
        select = grid[i][y]
        if select >= top:
            down = False
            break

    up = True
    for i in reversed(range(0, x)):
        select = grid[i][y]
        if select >= top:
            up = False
            break

    right = True
    for j in range(y+1, len(grid)):
        select = grid[x][j]
        if select >= top:
            right = False
            break

    left = True
    for j in reversed(range(0, y)):
        select = grid[x][j]
        if select >= top:
            left = False
            break

    return left or right or up or down


def visible(grid):
    size = len(grid)
    result = np.ones((size, size), bool).tolist()
    for i in range(1, size-1):
        for j in range(1, size-1):
            result[i][j] = calculateVisibility(grid, (i, j))
    return result


def countGrid(grid):
    count = 0
    size = len(grid)
    for i in range(0, size):
        for j in range(0, size):
            if grid[i][j]:
                count += 1
    return count


def scenic(grid, choord):
    x, y = choord
    top = grid[x][y]

    tally = 0
    for i in range(x+1, len(grid)):
        tally += 1
        select = grid[i][y]
        if select >= top or i == len(grid):
            break
    down = tally

    tally = 0
    for i in reversed(range(0, x)):
        select = grid[i][y]
        tally += 1
        if select >= top or i == 0:
            break
    up = tally

    tally = 0
    for j in range(y+1, len(grid)):
        select = grid[x][j]
        tally += 1
        if select >= top or j == len(grid):
            break
    right = tally

    tally = 0
    for j in reversed(range(0, y)):
        select = grid[x][j]
        tally += 1
        if select >= top or j == 0:
            break
    left = tally
    return left * up * right * down


if __name__ == "__main__":
    with open("day_08/input.txt") as file:
        text = file.read()
        grid = gridify(text)
        vis = visible(grid)
        part1 = countGrid(vis)
        print(f"Part1: {part1}")

        part2 = 0
        part2 = 0
        size = len(grid)
        for i in range(0, size):
            for j in range(0, size):
                part2 = max(scenic(grid, (i, j)), part2)

        print(f"Part2: {part2}")
