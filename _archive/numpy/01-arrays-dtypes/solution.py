import numpy as np


def create_checkerboard(n: int) -> np.ndarray:
    pass


def reshape_safe(arr: np.ndarray, shape: tuple) -> np.ndarray | None:
    pass


def dtype_report(arr: np.ndarray) -> dict:
    pass


def memory_efficient_range(start: int, stop: int, step: int) -> np.ndarray:
    pass


if __name__ == "__main__":
    print("=== create_checkerboard ===")
    print(create_checkerboard(4))

    print("\n=== reshape_safe ===")
    print(reshape_safe(np.arange(12), (3, 4)))
    print(reshape_safe(np.arange(12), (5, 5)))

    print("\n=== dtype_report ===")
    print(dtype_report(np.zeros((3, 4), dtype=np.float32)))

    print("\n=== memory_efficient_range ===")
    r = memory_efficient_range(0, 100, 1)
    print(f"dtype: {r.dtype}, len: {len(r)}")
    r = memory_efficient_range(0, 300, 1)
    print(f"dtype: {r.dtype}, len: {len(r)}")
