from collections import defaultdict
from itertools import permutations
from lib.Intcode import Intcode

with open("data/7.txt") as f:
    program = list(map(int, f.readline().split(",")))


# print(program)
computer = Intcode(program, False)

# options = list(permutations([0, 1, 2, 3, 4]))
options = list(permutations([5, 6, 7, 8, 9]))
# print(options)

max_thrust = 0

for option in options:
    # print("***Option: ", option)
    debug = False
    ampA = Intcode(program, option[0], debug)
    ampB = Intcode(program, option[1], debug)
    ampC = Intcode(program, option[2], debug)
    ampD = Intcode(program, option[3], debug)
    ampE = Intcode(program, option[4], debug)

    amplifiers = [ampA, ampB, ampC, ampD, ampE]
    input = 0

    while True:
        last = False
        for amp in amplifiers:
            # print("Run: ", amp, input)
            finish, input = amp.run(input)
            last = finish
        if last:
            # print(last)
            break
        # break

    # print("*Result: ", input)
    max_thrust = max(input, max_thrust)

print(max_thrust)