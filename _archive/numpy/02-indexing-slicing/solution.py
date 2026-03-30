import numpy as np


def extract_diagonal_blocks(mat: np.ndarray, block_size: int) -> list[np.ndarray]:
    pass


def mask_outliers(arr: np.ndarray, n_std: float) -> np.ndarray:
    pass


def fancy_select(arr: np.ndarray, row_indices: list, col_indices: list) -> np.ndarray:
    pass


def is_view(a: np.ndarray, b: np.ndarray) -> bool:
    pass


if __name__ == "__main__":
    print("=== extract_diagonal_blocks ===")
    m = np.arange(16).reshape(4, 4)
    print(extract_diagonal_blocks(m, 2))

    print("\n=== mask_outliers ===")
    a = np.array([1.0, 2.0, 3.0, 100.0, 2.5])
    print(mask_outliers(a, 1.5))

    print("\n=== fancy_select ===")
    m = np.arange(12).reshape(3, 4)
    print(fancy_select(m, [0, 1, 2], [3, 2, 1]))

    print("\n=== is_view ===")
    a = np.arange(10)
    print(is_view(a, a[::2]))
    print(is_view(a, a[[1, 3]]))
