directions = open("data.txt", "r").readline().strip()

def count_gifts(starting_idx=0, increment=1):
    coords = set()
    x, y = 0, 0
    coords.add((x, y))

    for idx in range(starting_idx, len(directions), increment):
        direction = directions[idx]
        if direction == "^":
            y += 1
        elif direction == "v":
            y -= 1
        elif direction == "<":
            x -= 1
        else:
            x += 1
        coords.add((x, y))
    return coords

print("Part 1: ", len(count_gifts()))
print("Part 2: ", len(count_gifts(0, 2) | count_gifts(1, 2)))
