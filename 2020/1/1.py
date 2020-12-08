from itertools import combinations
from common import multiply


data = [int(line.strip()) for line in open("data.txt", "r")]

for n in [2, 3]:
    print([multiply(a) for a in combinations(data, n) if sum(a) == 2020][0])
