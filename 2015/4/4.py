import hashlib

SECRET_KEY = open("data.txt", "r").readline().strip()

def calculate(leding_zeros):
    value = 1
    while True:
        key = SECRET_KEY + str(value)
        # print(key)
        if hashlib.md5(key.encode("utf-8")).hexdigest().startswith("0" * leding_zeros):
            return(value)
        value += 1

print("Part 1: ", calculate(5))
print("Part 2: ", calculate(6))