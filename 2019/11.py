from lib.Intcode import Intcode

with open("data/11.txt") as f:
    _program = list(map(int, f.readline().split(",")))

computer = Intcode(_program, debug=True)

SIZE = 50
data = [[0] * SIZE for i in range(SIZE)]

START = 5

BLACK = 0
WHITE = 1

x = START
y = START

UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)


def print_data(d):
    for line in d:
        print(line)


directions = (UP, RIGHT, DOWN, LEFT)
direction = 0
count = 0
data[y][x] = 1
while computer.is_running:
    input = data[y][x]
    if input == -1:
        count += 1
        input = 0
    print("Input:", input)
    color = computer.run(input)
    turn = computer.run()
    data[y][x] = color
    # print(color, turn)
    direction = ((direction + 1) % 4) if turn != 0 else ((direction - 1) % 4)
    x += directions[direction][0]
    y += directions[direction][1]

print_data(data)

for i, line in enumerate(data):
    if all(item == -1 for item in line):
        # print("True")
        data[i] = []

for line in data:
    print(line)
print(count)
