import numpy as np


def solve_system(A: np.ndarray, b: np.ndarray) -> np.ndarray | None:
    pass


def fit_line(x: np.ndarray, y: np.ndarray) -> tuple[float, float]:
    pass


def pca_reduce(data: np.ndarray, n_components: int) -> np.ndarray:
    pass


def matrix_power_stable(mat: np.ndarray, n: int) -> np.ndarray:
    pass


if __name__ == "__main__":
    print("=== solve_system ===")
    A = np.array([[2, 1], [5, 3]], dtype=float)
    b = np.array([4, 7], dtype=float)
    print(solve_system(A, b))

    print("\n=== fit_line ===")
    x = np.array([1, 2, 3, 4, 5], dtype=float)
    y = np.array([2.1, 3.9, 6.2, 7.8, 10.1])
    print(fit_line(x, y))

    print("\n=== pca_reduce ===")
    data = np.random.randn(100, 5)
    print(f"shape: {pca_reduce(data, 2).shape}")

    print("\n=== matrix_power_stable ===")
    m = np.array([[1, 1], [0, 1]], dtype=float)
    print(matrix_power_stable(m, 3))
