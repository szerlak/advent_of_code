data = [line.strip() for line in open('5.txt')]


def convert_binary_seat_to_decimal(binary):
    binary = binary.replace("F", "0")
    binary = binary.replace("B", "1")
    binary = binary.replace("L", "0")
    binary = binary.replace("R", "1")
    return int(binary[:7], 2), int(binary[-3:], 2)


def calculate_id(row, column):
    return row * 8 + column


max_id = 0
min_id = 1000
seats = set()
for seat in data:
    row, column = convert_binary_seat_to_decimal(seat)
    id = calculate_id(row, column)
    min_id, max_id = min(min_id, id), max(max_id, id)
    seats.add(id)

print(max_id)
print(list(set(range(min_id, max_id)) - seats)[0])


# ############ TESTS ###############
assert convert_binary_seat_to_decimal("BFFFBBFRRR") == (70, 7)
assert convert_binary_seat_to_decimal("FFFBBBFRRR") == (14, 7)
assert convert_binary_seat_to_decimal("BBFFBBFRLL") == (102, 4)
