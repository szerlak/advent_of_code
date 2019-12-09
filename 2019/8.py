import collections


with open("data/8.txt") as f:
    data = f.readline()


WIDTH = 25
HEIGHT = 6

size = WIDTH * HEIGHT
layers = [data[i:i+size] for i in range(0, len(data), size)]

# ############ PART 1 ###################
count = []
for layer in layers:
    d = collections.defaultdict(int)
    for c in layer:
        d[c] += 1
    count.append(d)

min_idx = 0
min_value = 9999999999
for idx, layer in enumerate(count):
    if layer.get("0", 0) < min_value:
        min_value = layer.get("0", 0)
        min_idx = idx
print(count[min_idx].get("1") * count[min_idx].get("2"))

# ############ PART 2 ###################
result = []
for i in range(0, size):
    for layer in layers:
        if layer[i] != "2":
            result.append(layer[i])
            break

assert len(result) == len(layers[0])

image = [result[i:i+WIDTH] for i in range(0, len(result), WIDTH)]
for line in image:
    for pixel in line:
        print(pixel, end=' ')
    print()
