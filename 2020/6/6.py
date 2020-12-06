from collections import Counter

# data = [line.strip() for line in open('6.txt')]
with open("6.txt", "r") as f:
    data = f.read().split("\n\n")

# ### PART 1
result_1 = 0
for block in data:
    c = Counter()
    for line in block.split("\n"):
        c.update(line)
    result_1 += len(c)

print(result_1)


# ### Part 2
result_2 = 0
for block in data:
    c = Counter()
    lines = block.split()
    people = len(lines)
    for line in lines:
        c.update(line)
    result_2 += sum(answer == people for _, answer in c.items())

print(result_2)