import numpy as np


def seeded_split(
    data: np.ndarray, train_ratio: float, seed: int
) -> tuple[np.ndarray, np.ndarray]:
    pass


def bootstrap_mean_ci(
    data: np.ndarray, n_bootstrap: int, confidence: float, seed: int
) -> tuple[float, float]:
    pass


def simulate_random_walk(n_steps: int, n_walks: int, seed: int) -> np.ndarray:
    pass


def weighted_sample_without_replacement(
    items: np.ndarray, weights: np.ndarray, k: int, seed: int
) -> np.ndarray:
    pass


if __name__ == "__main__":
    print("=== seeded_split ===")
    data = np.arange(10)
    train, test = seeded_split(data, 0.8, seed=42)
    print(f"train({len(train)}): {train}, test({len(test)}): {test}")

    print("\n=== bootstrap_mean_ci ===")
    data = np.array([2, 4, 6, 8, 10], dtype=float)
    lo, hi = bootstrap_mean_ci(data, 10000, 0.95, seed=42)
    print(f"95% CI: ({lo:.2f}, {hi:.2f})")

    print("\n=== simulate_random_walk ===")
    walks = simulate_random_walk(100, 5, seed=42)
    print(f"shape: {walks.shape}, final positions: {walks[:, -1]}")

    print("\n=== weighted_sample_without_replacement ===")
    items = np.array(["a", "b", "c", "d", "e"])
    weights = np.array([10, 1, 1, 1, 1])
    print(weighted_sample_without_replacement(items, weights, 3, seed=42))
