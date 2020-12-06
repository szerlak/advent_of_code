from collections import deque

from lib.Intcode2 import Intcode
from lib.utils import print_array

SIZE = 30
xy = [[-1] * SIZE for i in range(SIZE)]

with open("data/19.txt") as f:
    _program = list(map(int, f.readline().split(",")))


min_x = 0
max_x = 0
y = 0
count = 0
MIN_SIZE = 100
size_flag = False

arr_y = []

while True:
    # print(y)
    hash_flag = False
    x = min_x
    if max_x < min_x:
        max_x = min_x
    while x < max_x + 20:
        computer = Intcode(_program)
        computer.set_input([x, y])
        out = computer.run()
        # xy[y][x] = out
        if out == 1 and not hash_flag:
            hash_flag = True
            min_x = x
            x = max_x
            x += 1
            continue
        # if max_x - min_x > MIN_SIZE:
            # size_flag = True
            # print(y)
        if out == 0 and hash_flag:
            max_x = x
            break
        x += 1
    arr_y.append((min_x, max_x))
    if y > MIN_SIZE:
        x1, x2 = arr_y[y - MIN_SIZE + 1]
        x3, x4 = min_x, max_x
        if x3 + MIN_SIZE <= x2:
            print("RESULT:", x3, y - MIN_SIZE + 1)
            print("RESULT calculated:", x3 * 10000 + (y - MIN_SIZE + 1))
            break
    y += 1

# print_array(xy)