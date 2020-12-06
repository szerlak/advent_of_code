
from lib.Intcode_17 import Intcode

SCAFFOLD = "#"
OPEN = "."

with open("data/21.txt") as f:
    _program = list(map(int, f.readline().split(",")))


# D ^ ~C ^ ~A
part_1 = """NOT C J
AND D J
NOT A T
OR T J
WALK
"""

# D ^ H ^ ~(B ^ C) ^ ~A
part_2 = """OR B T
AND C T
NOT T J
AND D J
AND H J
NOT A T
OR T J
RUN
"""

# print(jump)


def run_droid(code):
    computer = Intcode(_program)
    out = None
    computer.set_data(code)
    while computer.is_running:
        o = computer.run()
        if o:
            out = o
    print(out)


run_droid(part_1)
run_droid(part_2)
