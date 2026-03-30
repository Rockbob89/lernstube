from functools import wraps


def retry(max_attempts=3):
    pass


if __name__ == "__main__":
    attempts = 0

    @retry(max_attempts=3)
    def flaky():
        global attempts
        attempts += 1
        if attempts < 3:
            raise ValueError("not yet")
        return "ok"

    print(flaky())  # → ok
