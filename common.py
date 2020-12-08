
def get_year(date):
    return date[0]


def get_day(date):
    return date[1]


def get_data(date):
    y = get_year(date)
    d = get_day(date)
    for line in open("./data/%s.txt" % d):
        yield line


def print_result(result, stage):
    print("Star %s: %s" % (stage, result))


def multiply(values):
    result = 1
    for value in values:
        result *= value
    return result
