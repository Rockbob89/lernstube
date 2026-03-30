import time
import tempfile
import shutil
from contextlib import contextmanager


class Timer:
    pass

@contextmanager
def tempdir():
    pass

class DatabaseConnection:
    pass


if __name__ == "__main__":
    # Timer
    with Timer() as t:
        time.sleep(0.1)
    print(f"elapsed: {t.elapsed:.2f}s")

    # tempdir
    with tempdir() as path:
        print(f"tempdir: {path}")
    print("tempdir cleaned up")

    # DatabaseConnection
    db = DatabaseConnection("mydb")
    with db:
        print(f"connected: {db.connected}")
        db.execute("SELECT 1")
    print(f"connected: {db.connected}")
    print(f"queries: {db.queries}")
