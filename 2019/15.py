from lib.Intcode import Intcode
from lib.utils import print_array
from collections import deque

with open("data/15.txt") as f:
    _program = list(map(int, f.readline().split(",")))

computer = Intcode(_program, debug=False)

SIZE = 50
xy = [[-1] * SIZE for i in range(SIZE)]

# print_array(xy, SIZE)

DIRECTION = {
    1: (-1, 0),  # NORTH
    2: (1, 0),  # SOUTH
    3: (0, -1),  # WEST
    4: (0, 1),  # EAST

}

direction = 1
robot_x, robot_y = SIZE // 2, SIZE // 2
xy[robot_x][robot_y] = 9


def move_dfs(x, y, direction, computer, path):
    new_computer = computer.clone()
    if new_computer.is_running:
        response = new_computer.run(direction)
        dx, dy = DIRECTION.get(direction)
        if response == 0:
            xy[x + dx][y + dy] = 0  # wall, don't change robot position
            return []
        if response == 1:
            x += dx
            y += dy
            xy[x][y] = 1  # empty space
        if response == 2:
            x += dx
            y += dy
            xy[x][y] = 2
            return path.copy()
        for dir in DIRECTION.keys():
            dx, dy = DIRECTION.get(dir)
            new_x = x + dx
            new_y = y + dy
            if xy[new_x][new_y] == -1:
                new_path = path.copy()
                new_path.append(dir)
                p = move_dfs(x, y, dir, new_computer, new_path)
                if p:
                    return p


# path = list()
# path.append(3)
# result = move_dfs(robot_x, robot_y, 3, computer, path)
# print_array(xy, SIZE)
# print(len(result))


oxygen = (0, 0)


def move_all(x, y, direction, computer):
    global oxygen
    new_computer = computer.clone()
    if new_computer.is_running:
        response = new_computer.run(direction)
        dx, dy = DIRECTION.get(direction)
        if response == 0:
            xy[x + dx][y + dy] = 0  # wall, don't change robot position
            return False
        if response == 1:
            x += dx
            y += dy
            xy[x][y] = 1  # empty space
        if response == 2:
            x += dx
            y += dy
            xy[x][y] = 2  # Finish
            oxygen = (x, y)
        for dir in DIRECTION.keys():
            dx, dy = DIRECTION.get(dir)
            new_x = x + dx
            new_y = y + dy
            if xy[new_x][new_y] == -1:
                move_all(x, y, dir, new_computer)


move_all(robot_x, robot_y, 3, computer)
print_array(xy, SIZE)

move_queue = deque()
count = 1000
move_queue.append((oxygen[0], oxygen[1], count))

max_count = 0
xy[oxygen[0]][oxygen[1]] = count

while move_queue:
    x, y, count = move_queue.popleft()
    if xy[x][y] == 0:
        continue
    max_count = max(max_count, count)
    for direction in DIRECTION.keys():
        dx, dy = DIRECTION.get(direction)
        new_x = x + dx
        new_y = y + dy
        if xy[new_x][new_y] == 1 or xy[new_x][new_y] == 2:
            xy[new_x][new_y] = count
            move_queue.append((x+dx, y+dy, count+1))

print(max_count - 1000)