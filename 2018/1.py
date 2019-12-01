from common import get_data

today = (2018, 1)


def frequency(data):
    counter = 0
    for freq in data:
        counter += int(freq)
    return counter


def find_repeat_freq(data):
    # print(data)
    counter = 0
    repeat = {0}
    while True:
        for freq in data:
            f = int(freq)
            counter += f
            # print(counter, repeat)
            if counter in repeat:
                # print(counter)
                return counter
            repeat.add(counter)


assert frequency(["+1", "+1", "+1"]) == 3
assert frequency(["+1", "+1", "-2"]) == 0
assert frequency(["-1", "-2", "-3"]) == -6

assert find_repeat_freq(["+1", "-1"]) == 0
assert find_repeat_freq([+3, +3, +4, -2, -4]) == 10
assert find_repeat_freq([-6, +3, +8, +5, -6]) == 5
assert find_repeat_freq([+7, +7, -2, -7, -4]) == 14


def main():
    _input = get_data(today)
    data = []
    for i in _input:
        data.append(i)
    print(frequency(data))
    print(find_repeat_freq(data))


if __name__ == "__main__":
    main()
