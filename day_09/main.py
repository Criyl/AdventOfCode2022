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
    elif abs(dx) == 1 and abs(dy) == 2:
        delta = (dx, dy/2)
    else:
        delta = (dx/2, dy/2)

    return (int(tail[0]+delta[0]), int(tail[1]+delta[1]))


def iterate(direction, lastrope):
    rope = lastrope.copy()

    x, y = rope[0]

    if direction == 'L':
        x -= 1
    if direction == 'U':
        y += 1
    if direction == 'R':
        x += 1
    if direction == 'D':
        y -= 1

    newhead = (x, y)
    rope[0] = newhead

    for i in range(1, len(rope)):
        rope[i] = predict(rope[i-1], rope[i])

    return rope


def generatePath(steps, n=2):
    history = []
    rope = [(0, 0)]

    for _ in range(n-1):
        rope.append((0, 0))

    history.append(rope)

    for line in steps.splitlines():
        direction, length = line.split(' ')
        for _ in range(0, int(length)):
            rope = iterate(direction, rope)
            history.append(rope)
    return history


if __name__ == "__main__":
    with open("day_09/input.txt") as file:
        text = file.read()
        history = generatePath(text, 10)
        mapped = map(lambda rope: rope[9], history)
        print(len(set(mapped)))
