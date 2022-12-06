highest = 0
with open("input.txt") as file:
    count = 0
    for line in file.readlines():
        stripped = line.strip()
        if stripped == '':
            highest = max(count, highest)
            count = 0
        else:
            num = int(line.strip())
            count += num

print(highest)