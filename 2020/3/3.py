from functools import reduce
from operator import mul

data = [line.strip() for line in open("data.txt", "r")]

slopes = ((3, 1), (1, 1), (5, 1), (7, 1), (1, 2))

solutions = []
for dx, dy in slopes:
    count = x = y = 0
    while y < len(data):
        if data[y][x] == "#":
            count += 1
        x = (x + dx) % len(data[0])
        y += dy
    solutions.append(count)

print(solutions[0])
print(reduce(mul, solutions))

