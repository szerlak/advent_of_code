from collections import deque
from lib.utils import timeit

with open("data/16.txt") as f:
    input = f.readline()


@timeit
def part_1():
    numbers = [int(num) for num in str(input)]
    NUM_SIZE = len(numbers)

    for _ in range(100):
        for idx in range(NUM_SIZE):
            pattern = deque([i for i in [0, 1, 0, -1] for _ in range(idx + 1)])
            pattern.rotate(-1)
            value = 0
            for number in numbers:
                value += number * pattern[0]
                pattern.rotate(-1)
            numbers[idx] = abs(value) % 10

    return "".join(str(i) for i in numbers[:8])

@timeit
def part_2():
    modified_input = str(input) * 10000
    offset = int(input[:7])
    numbers = [int(num) for num in modified_input][offset:]
    numbers.reverse()

    for _ in range(100):
        val = 0
        for idx in range(len(numbers)):
            val = (val + numbers[idx]) % 10
            numbers[idx] = val
    numbers.reverse()
    return "".join(str(i) for i in numbers[:8])

@timeit
def part_2b():
    modified_input = str(input) * 10000
    offset = int(input[:7])
    numbers = [int(num) for num in modified_input][offset:]

    for _ in range(100):
        for idx in range(-2, -len(numbers)-1, -1):
            numbers[idx] = (numbers[idx] + numbers[idx+1]) % 10
    return "".join(str(i) for i in numbers[:8])


# print(part_1())
print(part_2())  # 19422575
print(part_2b())  # 19422575
