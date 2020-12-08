from itertools import accumulate
data = open("data.txt", "r").readline().strip()
converted_data = [1 if ch == "(" else -1 for ch in data]

print(sum(converted_data))
print(list(accumulate(converted_data)).index(-1) + 1)
