from common import get_data, print_result

today = (2018, 1)


def fuel(n):
    return max(int(int(n)/3)-2, 0)


def star_1(data):
    result = 0
    for i in data:
        result += fuel(i)
    return result


def star_2(data):
    result = 0
    for i in data:
        t = fuel(i)
        while t > 0:
            result += t
            t = fuel(t)
    return result


def main():
    _input = get_data(today)
    data = []
    for i in _input:
        data.append(i)
    print_result(star_1(data), 1)
    print_result(star_2(data), 2)


if __name__ == "__main__":
    main()


assert fuel(14) == 2
assert fuel(2) == 0

assert star_1([14, 14]) == 4

assert star_2([1969]) == 966
assert star_2([100756]) == 50346
