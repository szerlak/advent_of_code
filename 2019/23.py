from collections import deque

from lib.Intcode2 import Intcode, NoInputException

with open("data/23.txt") as f:
    _program = list(map(int, f.readline().split(",")))


computers = []
queues = []
for i in range(50):
    computers.append(Intcode(_program, setting=i))
    queues.append(deque([]))


nat = (-1, -1)
flag = True
delivered = set()

while True:
    flag = True
    for i, computer in enumerate(computers):
        # print("Computer", i)
        try:
            x = queues[i].popleft()
            y = queues[i].popleft()
            item = [x, y]
            flag = False
        except IndexError:
            item = [-1]
        # print("Items", item)
        computer.set_input(item)
        while True:
            try:
                address = computer.run()
                x = computer.run()
                y = computer.run()
            except NoInputException:
                break
            if address < 50:
                queues[address].append(x)
                queues[address].append(y)
            if address == 255:
                print("NAT")
                nat = (x, y)
    print("Loop finished")
    if flag:
        print("IDLE")
        if nat[1] in delivered:
            print("RESULT", nat[1])
            break
        delivered.add(nat[1])
        queues[0].append(nat[0])
        queues[0].append(nat[1])
