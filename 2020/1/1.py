from operator import mul
from itertools import combinations
from functools import reduce

data = [int(line.strip()) for line in open("data.txt", "r")]

for n in [2, 3]:
    print([reduce(mul, a) for a in combinations(data, n) if sum(a) == 2020][0])
