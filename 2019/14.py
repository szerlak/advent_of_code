from collections import defaultdict
from math import ceil
from lib.utils import timeit

rules = defaultdict(list)
with open("data/14.txt") as f:
    for line in f:
        l, r = line.strip().split(" => ")
        elements = l.split(", ")
        for e in elements:
            rules[r].append(e)

# print(rules)

def count(el="ORE", fuel=1):
    if el == "FUEL":
        return fuel
    q = 0
    for output, elements in rules.items():
        for element in elements:
            quantity, item = element.split()
            if el == item:
                # print(element, "=>", output)
                parent_quantity, parent = output.split()
                q += ceil(count(parent, fuel) / int(parent_quantity)) * int(quantity)
    # print(el, q)
    return q

@timeit
def part_1():
    print(count())

@timeit
def part_2():
    ORE_MAX = 1_000_000_000_000
    fuel_min, fuel_max = 1, 100_000_000

    while (fuel_max - fuel_min) > 1:
        middle = (fuel_min + fuel_max) // 2
        if count(fuel=middle) <= ORE_MAX:
            fuel_min = middle
        else:
            fuel_max = middle

    print(fuel_min)

part_1()
part_2()
