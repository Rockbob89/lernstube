import numpy as np


def column_zscore(mat: np.ndarray) -> np.ndarray:
    pass


def rolling_mean(arr: np.ndarray, window: int) -> np.ndarray:
    pass


def top_k_per_row(mat: np.ndarray, k: int) -> np.ndarray:
    pass


def nan_aware_summary(arr: np.ndarray) -> dict:
    pass


if __name__ == "__main__":
    print("=== column_zscore ===")
    m = np.array([[1, 2], [3, 4], [5, 6]], dtype=float)
    print(column_zscore(m))

    print("\n=== rolling_mean ===")
    print(rolling_mean(np.array([1, 2, 3, 4, 5], dtype=float), 3))

    print("\n=== top_k_per_row ===")
    m = np.array([[3, 1, 4, 1, 5], [9, 2, 6, 5, 3]])
    print(top_k_per_row(m, 3))

    print("\n=== nan_aware_summary ===")
    a = np.array([1.0, np.nan, 3.0, 4.0, np.nan, 6.0])
    print(nan_aware_summary(a))
