from common import get_data

today = (2017, 1)


def captcha(data: str, offset: int = 1) -> int:
    count = 0
    for x, y in zip(data, data[offset:] + data[:offset]):
        if x == y:
            count += int(x)
    return count


assert captcha('1122') == 3


def main():
    _input = get_data(today)
    data = next(_input)
    print(captcha(data))
    print(captcha(data, len(data)//2))


if __name__ == "__main__":
    main()
