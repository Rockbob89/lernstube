import time
from functools import wraps


def timer(fn):
    pass


if __name__ == "__main__":
    @timer
    def slow():
        time.sleep(0.1)
        return "done"

    result = slow()
    print(result)         # → done
    print(slow.__name__)  # → slow
