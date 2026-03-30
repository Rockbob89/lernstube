import time
import functools


def counter():
    pass

def timer(func):
    pass

def retry(max_attempts=3):
    pass

def validate_types(**type_kwargs):
    pass


if __name__ == "__main__":
    # counter
    c = counter()
    print(c(), c(), c())

    # timer
    @timer
    def slow():
        time.sleep(0.1)
        return "done"
    print(slow())

    # retry
    attempts = 0
    @retry(max_attempts=3)
    def flaky():
        global attempts
        attempts += 1
        if attempts < 3:
            raise ValueError("not yet")
        return "ok"
    print(flaky())

    # validate_types
    @validate_types(name=str, age=int)
    def register(name, age):
        return f"{name} is {age}"
    print(register(name="Alice", age=30))
