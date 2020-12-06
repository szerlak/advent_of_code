from itertools import permutations
from math import gcd


def lcm(x, y):
    return (x*y)//gcd(x, y)

class Moon:
    def __init__(self, name, x, y, z):
        self.name = name
        self.init_x = x
        self.init_y = y
        self.init_z = z
        self.x = x
        self.y = y
        self.z = z
        self.vx = 0
        self.vy = 0
        self.vz = 0

    def __str__(self):
        return self.name

    def print_status(self):
        print("{:10s} pos=<{:2d}, {:3d}, {:3d}>, vel=<{:3d}, {:3d}, {:3d}>".format(
            self.name, self.x, self.y, self.z, self.vx, self.vy, self.vz)
        )

    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

    def get_position(self):
        return self.x, self.y, self.z

    def get_velocity(self):
        return self.vx, self.vy, self.vz

    def get_potential_energy(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def get_kinetic_energy(self):
        return abs(self.vx) + abs(self.vy) + abs(self.vz)

    def get_energy(self):
        return self.get_potential_energy() * self.get_kinetic_energy()

    @staticmethod
    def _adjust_axis(x, x2):
        if x < x2:
            return 1
        if x > x2:
            return -1
        return 0

    def adjust_velocity(self, pos):
        self.vx += self._adjust_axis(self.x, pos[0])
        self.vy += self._adjust_axis(self.y, pos[1])
        self.vz += self._adjust_axis(self.z, pos[2])



# m1 = Moon("Io", -1, 0, 2)
# m2 = Moon("Europa", 2, -10, -7)
# m3 = Moon("Ganymede", 4, -8, 8)
# m4 = Moon("Callisto", 3, 5, -1)

# m1 = Moon("Io", -8, -10, 0)
# m2 = Moon("Europa", 5, 5, 10)
# m3 = Moon("Ganymede", 2, -7, 3)
# m4 = Moon("Callisto", 9, -8, -3)

m1 = Moon("Io", 16, -8, 13)
m2 = Moon("Europa", 4, 10, 10)
m3 = Moon("Ganymede", 17, -5, 6)
m4 = Moon("Callisto", 13, -3, 0)

# init_m1 = [-1, 0, 2]
# init_m2 = [2, -10, -7]
# init_m3 = [4, -8, 8]
# init_m4 = [3, 5, -1]
#
# m1 = Moon("Io", init_m1[0], init_m1[1], init_m1[2])
# m2 = Moon("Europa", init_m2[0], init_m2[1], init_m2[2])
# m3 = Moon("Ganymede", init_m3[0], init_m3[1], init_m3[2])
# m4 = Moon("Callisto", init_m4[0], init_m4[1], init_m4[2])

moons = [m1, m2, m3, m4]
pairs = list(permutations(moons, 2))

count = 0
cycle_x = 0
cycle_y = 0
cycle_z = 0


def check_cycle(axis):
    br = False
    for moon in moons:
        axis_value = moon.__getattribute__(axis)
        axis_init = moon.__getattribute__("init_{}".format(axis))
        velocity = moon.__getattribute__("v{}".format(axis))
        if axis_value != axis_init or velocity != 0:
            return False
    return True


# for i in range(0, 100000):
while True:
    count += 1
    break_flag = True
    # print("======STEP {} ======".format(i + 1))
    for moon1, moon2 in pairs:
        moon1.adjust_velocity(moon2.get_position())
    for i, moon in enumerate(moons):
        moon.move()
        if cycle_x == 0 and check_cycle("x"):
            cycle_x = count
        if cycle_y == 0 and check_cycle("y"):
            cycle_y = count
        if cycle_z == 0 and check_cycle("z"):
            cycle_z = count
    # if all(c != 0 for c in cycle_x) and all(c != 0 for c in cycle_y) and all(c != 0 for c in cycle_z):
    if cycle_x != 0 and cycle_y != 0 and cycle_z != 0:
        break


# print(sum(moon.get_energy() for moon in moons))
print(cycle_x, cycle_y, cycle_z)
print(lcm(lcm(cycle_x, cycle_y), cycle_z))