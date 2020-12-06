from common import get_data
from lib.Intcode import Intcode

today = (2018, 2)

initial = []


def main():
    _input = get_data(today)
    data = []
    for i in _input:
        data.append(i)
    for i in data[0].split(","):
        initial.append(int(i))

    program = initial.copy()
    program[1] = 12
    program[2] = 2
    a = Intcode(program, None)
    print(a.run(0))

    for x in range(100):
        for y in range(100):
            program = initial.copy()
            program[1] = x
            program[2] = y
            a = Intcode(program, None)
            result = a.run(0)['program']
            if result == 19690720:
                print(100 * x + y)
                return


if __name__ == "__main__":
    main()
