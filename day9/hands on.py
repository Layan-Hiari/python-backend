import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration = end - start
        print(f"Function '{func.__name__}' took {duration:.4f} seconds to run.")
        return result
    return wrapper
