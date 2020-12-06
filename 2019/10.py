from collections import defaultdict
import heapq
from math import gcd, atan2, degrees

input = []
with open("data/10.txt") as f:
    for line in f:
        input.append(line.strip())

HEIGHT = len(input)
WIDTH = len(input[0])

# print(HEIGHT)
# print(WIDTH)

data = [["."] * WIDTH for i in range(HEIGHT)]
for y, line in enumerate(input):
    for x, point in enumerate(line):
        data[y][x] = point

# for line in data:
#     print(line)

result = data.copy()

def calc_vector(x1, y1, x2, y2):
    x = x2 - x1
    y = y2 - y1
    divisor = gcd(x, y)
    if divisor == 0:
        return x, y
    dx = x // divisor
    dy = y // divisor
    return dx, dy

def calculate_visible(x1, y1):
    visible = set()
    for y2, line in enumerate(data):
        for x2, point in enumerate(line):
            if point == "#":
                visible.add(calc_vector(x1, y1, x2, y2))
    # print(x1, y1, visible)
    return visible


max_val = 0
max_x = 0
max_y = 0
for y, line in enumerate(data):
    for x, point in enumerate(line):
        if point == ".":
            continue
        val = len(calculate_visible(x, y))
        if val > max_val:
            max_val = val
            max_x = x
            max_y = y

print(max_val - 1, max_x, max_y)


# ############### PART 2 ################
def calculate_angle(x1, y1, x2, y2):
    x = x2 - x1
    y = y2 - y1
    return degrees(atan2(x, y))


# print(degrees(atan2(0, -1)))
# print(degrees(atan2(1, -1)))
# print(degrees(atan2(1, 0)))
# print(degrees(atan2(1, 1)))
# print(degrees(atan2(0, 1)))
# print(degrees(atan2(-1, 1)))
# print(degrees(atan2(-1, 0)))
# print(degrees(atan2(-1, -1)))

asteroids_by_angle = defaultdict(list)

# max_x = 2
# max_y = 3
#
data[max_y][max_x] = "X"

# for line in data:
#     print(line)

for y, line in enumerate(data):
    for x, point in enumerate(line):
        if point == ".":
            continue
        if x == max_x and y == max_y:
            continue
        angle = calculate_angle(max_x, max_y, x, y)
        distance = abs(x - max_x) + abs(y - max_y)
        heapq.heappush(asteroids_by_angle[angle], (distance, (x, y)))

# for angle, asteroids in asteroids_by_angle.items():
#     print(angle, asteroids)

angle = 181

for i in range(0, 300):
    angles = list(asteroids_by_angle.keys())
    angles.sort(reverse=True)
    for ang in angles:
        if angle > ang:
            angle = ang
            break
    else:
        angle = angles[0]
    # print(angle)
    asteroid = heapq.heappop(asteroids_by_angle[angle])
    if not asteroids_by_angle[angle]:
        del asteroids_by_angle[angle]
    print("#{}: {}deg, XY: {}, {}".format(i + 1, int(angle), asteroid[1][0], asteroid[1][1]))
