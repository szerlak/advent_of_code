from common import get_data


today = (2018, 8)


_in = get_data(today)
_input = next(_in)
# _input = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"


def value():
    for data in _input.split():
        yield int(data)


value_generator = value()


def validate_node():
    node_sum = 0
    nodes_count = next(value_generator)
    meta_count = next(value_generator)

    node_values = []

    for node in range(0, nodes_count):
        node_values.append(validate_node())

    for meta in range(0, meta_count):
        if nodes_count == 0:
            node_sum += next(value_generator)
        else:
            index = next(value_generator)
            try:
                node_sum += node_values[index - 1]
            except IndexError:
                pass
    return node_sum


print(validate_node())
