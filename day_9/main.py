
def predict(head, tail):
    dx = head[0] - tail[0]
    dy = head[1] - tail[1]
    delta = (0, 0)

    if abs(dx) <= 1 and abs(dy) <= 1:
        delta = (0, 0)
    elif dx == 0 or dy == 0:
        delta = (dx/2, dy/2)
    elif abs(dx) == 2 and abs(dy) == 1:
        delta = (dx/2, dy)
    else:
        delta = (dx, dy/2)

    return (int(tail[0]+delta[0]), int(tail[1]+delta[1]))


def generatePath(steps):
    tail = [(0, 0)]
    head = [(0, 0)]
    for line in steps.splitlines():
        direction, length = line.split(' ')
        for x in range(0, int(length)):
            x, y = head[len(head)-1]

            if direction == 'L':
                x -= 1
            if direction == 'U':
                y += 1
            if direction == 'R':
                x += 1
            if direction == 'D':
                y -= 1
            newhead = (x, y)
            head.append(newhead)
            i, j = tail[len(tail)-1]
            newtail = predict(newhead, (i, j))
            tail.append(newtail)
    return head, tail


if __name__ == "__main__":
    with open("day_9/input.txt") as file:
        text = file.read()
        heads, tails = generatePath(text)
        print(len(set(tails)))
