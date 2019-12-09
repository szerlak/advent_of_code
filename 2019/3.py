from common import get_data

today = (2018, 3)

SIZE = 20000
START = 10000

xy = [[0] * SIZE for i in range(SIZE)]
crossing = []
cable = [0, 0]


def draw_line(sx, sy, direction, size, num):
    star_x = sx
    star_y = sy
    for i in range(1, size+1):
        cable[num-1] += 1
        if direction == "D":
            if num == 2 and xy[sx][sy + i] > 0:
                crossing.append((sx, sy + i, xy[sx][sy + i] + cable[1]))
            if num == 1:
                xy[sx][sy + i] += cable[0]
            star_y += 1
        elif direction == "U":
            # xy[sx][sy - i] += num
            # star_y -= 1
            # if xy[sx][sy - i] == 3:
            #     crossing.append((sx, sy - i))
            if num == 2 and xy[sx][sy - i] > 0:
                crossing.append((sx, sy-i, xy[sx][sy - i] + cable[1]))
            if num == 1:
                xy[sx][sy - i] += cable[0]
            star_y -= 1
        elif direction == "R":
            # xy[sx + i][sy] += num
            # star_x += 1
            # if xy[sx + i][sy] == 3:
            #     crossing.append((sx + i, sy))
            if num == 2 and xy[sx+i][sy] > 0:
                crossing.append((sx+i, sy, xy[sx+i][sy] + cable[1]))
            if num == 1:
                xy[sx+i][sy] += cable[0]
            star_x += 1
        elif direction == "L":
            # xy[sx - i][sy] += num
            # star_x -= 1
            # if xy[sx - i][sy] == 3:
            #     crossing.append((sx - i, sy))
            if num == 2 and xy[sx-i][sy] > 0:
                crossing.append((sx-i, sy, xy[sx-i][sy] + cable[1]))
            if num == 1:
                xy[sx-i][sy] += cable[0]
            star_x -= 1
    # print_table()
    # print("*" * 50)
    # print(star_x, star_y)
    return star_x, star_y


def print_table():
    for y in range(0, SIZE):
        for x in range(0, SIZE):
            print(xy[x][y], end=' ')
        print()


def distance(x, y, x2, y2):
    return abs(x2 - x) + abs(y2 - y)


def main():
    _input = get_data(today)
    data = []
    for i in _input:
        data.append(i)

    cable_num = 0
    for d in data:
        cable_num += 1
        start_x = START
        start_y = START
        for move in d.split(","):
            (start_x, start_y) = draw_line(start_x, start_y, move[0], int(move[1:]), cable_num)
        # print(crossing)

    # print_table()
    dist = 999999999
    min_len = 999999
    for cross in crossing:
        print(cross[0], cross[1], cross[2])
        aaa = distance(START, START, cross[0], cross[1])
        print(aaa)
        dist = min(aaa, dist)
        min_len = min(cross[2], min_len)
    print(dist)
    print(min_len)


if __name__ == "__main__":
    main()
