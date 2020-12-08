data = [line.strip() for line in open("data.txt", "r")]


p1 = p2 = 0
for line in data:
    r, password = line.split(":")
    r, ch = r.split()
    r_min, r_max = map(int, r.split("-"))
    if r_min <= password.count(ch) <= r_max:
        p1 += 1
    if (password[r_min] == ch) ^ (password[r_max] == ch):
        p2 += 1

print(p1, p2)