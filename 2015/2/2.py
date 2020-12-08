from itertools import combinations
from common import multiply

data = [line.strip().split("x") for line in open("data.txt", "r")]
for idx, line in enumerate(data):
    data[idx] = sorted([int(i) for i in line])


def paper(package):
    sides = [multiply(side) for side in combinations(package, 2)]
    return 2 * sum(sides) + min(sides)


def ribbon(x, y, z):
    return 2 * (x + y) + x * y * z


print(sum([paper(package) for package in data]))
print(sum([ribbon(*package) for package in data]))
