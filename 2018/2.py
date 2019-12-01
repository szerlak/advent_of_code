from itertools import combinations

from common import get_data
from collections import Counter

today = (2018, 2)


def task_1(data):
    result = [0, 0]
    for word in data:
        counter = [j for i, j in Counter(word).most_common()]
        if 2 in counter:
            result[0] += 1
        if 3 in counter:
            result[1] += 1
    return result[0] * result[1]


assert task_1(["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]) == 12


def compare(w1, w2):
    diff_count = 0
    diff_index = -1
    for i in range(0, len(w1)):
        if w1[i] != w2[i]:
            diff_count += 1
            diff_index = i
        if diff_count > 1:
            return ""
    if diff_count == 0:
        return ""
    # Diff count == 1
    return w1[:diff_index] + w1[diff_index+1:]


def task_2(data):
    pairs = combinations(data, 2)
    for w1, w2 in pairs:
        result = compare(w1, w2)
        if result != "":
            return result


def main():
    _input = get_data(today)
    data = []
    for i in _input:
        data.append(i)

    print(task_1(data))
    print(task_2(data))


if __name__ == "__main__":
    main()
