from lib.Intcode import Intcode

with open("data/5.txt") as f:
    input = list(map(int, f.readline().split(",")))

computer = Intcode(input, False)
print(computer.run([1]))
print(computer.run([5]))