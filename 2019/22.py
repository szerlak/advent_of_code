from lib.utils import timeit

SIZE = 10
# SIZE = 10007
# SIZE = 119315717514047


moves = []
with open("data/22.txt") as f:
    for line in f:
        moves.append(line.strip())


# ========== Part 1
def cut(idx, num):
    return (idx - num) % SIZE


def deal_new_stack(idx):
    return SIZE - idx - 1


def deal_with_inc(idx, inc):
    return (inc * idx) % SIZE


# @timeit
def run(idx):
    index = idx
    for move in moves:
        if move.startswith("deal into new stack"):
            index = deal_new_stack(index)
        elif move.startswith("deal with increment"):
            inc = int(move.split()[-1])
            index = deal_with_inc(index, inc)
        else:
            num = int(move.split()[-1])
            index = cut(index, num)
    return index


# ========== Part 2
def reverse_cut(a, b, num):
    return a, b + num


def reverse_deal_new_stack(a, b):
    return -a, b-a


def reverse_deal_with_inc(a, b, inc):
    m = pow(inc, -1, SIZE)
    return a * m, b
# ========================


def run2(a, b):
    for move in moves:
        if move.startswith("deal into new stack"):
            a, b = reverse_deal_new_stack(a, b)
        elif move.startswith("deal with increment"):
            inc = int(move.split()[-1])
            a, b = reverse_deal_with_inc(a, b, inc)
        else:
            num = int(move.split()[-1])
            a, b = reverse_cut(a, b, num)
    return a % SIZE, b % SIZE


a, b = reverse_cut(2, 1, 3)
print([(a*i + b) % SIZE for i in range(10)])

# ROUNDS = 101741582076661
#
# a, b = run2(1, 0)
# print(a, b)
#
# aa = pow(a, ROUNDS, SIZE)
# bb = b * (1 - pow(a, ROUNDS, SIZE)) * pow(1 - a, -1, SIZE)
#
# print(aa, bb)
#
# index = 2020
# print((aa * index + bb) % SIZE)