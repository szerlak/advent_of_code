START=172930
END=683082

count = 0


for a in range(1, 10):
    for b in range(a, 10):
        for c in range(b, 10):
            for d in range(c, 10):
                for e in range(d, 10):
                    for f in range(e, 10):
                        repeat = 0
                        if a == b and b < c:
                            repeat += 1
                        if a < b and b == c and c < d:
                            repeat += 1
                        if b < c and c == d and d < e:
                            repeat += 1
                        if c < d and d == e and e < f:
                            repeat += 1
                        if d < e and e == f:
                            repeat += 1
                        if repeat >= 1:
                            num = 100000 * a + 10000 * b + 1000 * c + 100 * d + 10 * e + f
                            if START < num < END:
                                print(num)
                                count += 1

# 678899

print(count)
