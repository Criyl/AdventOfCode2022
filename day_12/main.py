def distance(first, second):
    if (first == 'S' and second == 'a') or (first == 'z' and second == 'E'):
        return 0
    if first == 'S' or second == 'E':
        return 999
    diff = ord(second) - ord(first)
    return diff


def buildGraph(text):
    graph = {}
    start = (-1, -1)
    lowest = []
    end = (-1, -1)
    rows = text.splitlines()
    for y, col in enumerate(rows):
        for x, char in enumerate(col):
            if char == 'S':
                start = (x, y)
            elif char == 'E':
                end = (x, y)
            elif char == 'a':
                lowest.append((x, y))

            connections = []

            if x+1 < len(col) and distance(char, col[x+1]) <= 1:
                connections += [(x+1, y)]
            if x-1 >= 0 and distance(char, col[x-1]) <= 1:
                connections += [(x-1, y)]
            if y-1 >= 0 and distance(char, rows[y-1][x]) <= 1:
                connections += [(x, y-1)]
            if y+1 < len(rows) and distance(char, rows[y+1][x]) <= 1:
                connections += [(x, y+1)]

            graph[(x, y)] = connections

    return graph, start, end, lowest


def search(graph, start, target):
    short_path = {}
    short_path[start] = [start]

    visited = set()
    explored = set()
    queue = [(None, start)]
    while queue != []:
        parent, node = queue.pop()
        visited.add(node)

        if parent is not None:
            newPath = short_path[parent]+[node]
            if node not in short_path or len(newPath) < len(short_path[node]):
                short_path[node] = short_path[parent]+[node]

        connections = graph[node]
        for connection in connections:
            if connection not in explored:
                entry = (node, connection)
                queue = [entry] + queue
                explored.add(connection)

    return short_path[target] if target in short_path else None


def solve(text, startOnly=True):
    graph, start, end, lowest = buildGraph(text)

    path = search(graph, start, end)

    shortest = path
    if not startOnly:
        for low in lowest:
            temp = search(graph, low, end)
            if temp and len(temp) < len(shortest):
                shortest = temp

    return shortest


if __name__ == "__main__":
    with open("day_12/input.txt") as file:
        text = file.read()

        path = solve(text)
        # print_path(path)
        print(len(path)-1)

        path2 = solve(text, part1=False)
        # print_path(path2)
        print(len(path2)-1)
