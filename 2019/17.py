from collections import deque

from lib.Intcode2 import Intcode
from lib.utils import print_array

SCAFFOLD = "#"
OPEN = "."

with open("data/17.txt") as f:
    _program = list(map(int, f.readline().split(",")))

# computer = Intcode(_program, debug=False)
#
# xy = [[]]
#
# while computer.is_running:
#     out = computer.run()
#     if not out:
#         break
#     if out == 10:
#         xy.append([])
#         continue
#     xy[len(xy) - 1].append(chr(out))
#
# xy = [x for x in xy if x]
#
# count = 0
# for y in range(2, len(xy) - 2):
#     for x in range(2, len(xy[0]) - 2):
#         if xy[y][x] == SCAFFOLD and \
#                 xy[y - 1][x] == SCAFFOLD and \
#                 xy[y + 1][x] == SCAFFOLD and \
#                 xy[y][x - 1] == SCAFFOLD and \
#                 xy[y][x + 1] == SCAFFOLD:
#             count += x * y
#
# print(count)
# print(print_array(xy))


inputs = "A,B,A,B,A,C,B,C,A,C\n" + \
    "L,6,R,12,L,6\n" + \
    "R,12,L,10,L,4,L,6\n" + \
    "L,10,L,10,L,4,L,6\n" + \
    "n\n"

commands = deque([ord(x) for x in inputs])
print(commands)

_program[0] = 2
computer = Intcode(_program)

out = None
computer.set_input(commands)
while computer.is_running:
    out = computer.run()
    print("Out", out)

print(out)
