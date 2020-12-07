from collections import defaultdict, deque
from functools import lru_cache

data = [line.strip() for line in open("data.txt", "r")]

contains_dict = defaultdict(list)
contained_by_dict = defaultdict(list)


for line in data:
    input, output = line[:-1].split(" contain ")
    if "no" in output:
        continue
    input_bag = tuple(input.split()[:-1])
    output_bags = [
        (int(line.split()[0]), tuple(line.split()[1:-1]))
        for line in output.split(",")
    ]
    contains_dict[input_bag] = output_bags
    for _, bag in output_bags:
        contained_by_dict[bag].append(input_bag)


# ####### Part 1 ##########
queue = deque([("shiny", "gold")])
solution = set()

while queue:
    bag = queue.popleft()
    solution.add(bag)
    queue.extend(contained_by_dict[bag])

print(len(solution) - 1)


# ####### Part 2 ##########
@lru_cache
def sum_bags(bag):
    counter = 1
    for count, item in contains_dict[bag]:
        counter += count * sum_bags(item)
    return counter


print(sum_bags(("shiny", "gold")) - 1)
