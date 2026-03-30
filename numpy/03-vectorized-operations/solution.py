import numpy as np


def pairwise_distances(points: np.ndarray) -> np.ndarray:
    pass


def normalize_rows(mat: np.ndarray) -> np.ndarray:
    pass


def apply_discount_matrix(prices: np.ndarray, discount_tiers: np.ndarray) -> np.ndarray:
    pass


def batch_polynomial(x: np.ndarray, coeffs: np.ndarray) -> np.ndarray:
    pass


if __name__ == "__main__":
    print("=== pairwise_distances ===")
    pts = np.array([[0, 0], [3, 4], [1, 1]])
    print(pairwise_distances(pts))

    print("\n=== normalize_rows ===")
    print(normalize_rows(np.array([[3.0, 4.0], [0.0, 0.0], [1.0, 0.0]])))

    print("\n=== apply_discount_matrix ===")
    print(apply_discount_matrix(np.array([100, 200]), np.array([0.1, 0.2, 0.3])))

    print("\n=== batch_polynomial ===")
    print(batch_polynomial(np.array([0, 1, 2]), np.array([2, 3, 1])))
