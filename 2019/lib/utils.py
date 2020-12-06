import functools
import time

def print_array(xy):
    size = len(xy[0])
    print("*" * (size+2))
    for line in xy:
        print("*", end='')
        for point in line:
            if point == -1:
                p = " "
            elif point == 0:
                p = "#"
            elif point == 1:
                p = "."
            elif point == 2:
                p = "F"
            elif point == 9:
                p = "S"
            else:
                p = point
            print(p, end='')
        print("*")
    print("*" * (size + 2))


def timeit(func):
    @functools.wraps(func)
    def timed(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in  {run_time:.4f} secs")
        return value
    return timed
