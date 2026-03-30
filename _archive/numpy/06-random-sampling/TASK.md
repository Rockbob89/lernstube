# Task 06: Random & Sampling

## Objective
Use NumPy's random module for reproducible random data generation and statistical sampling.

## What to Learn
- `np.random.default_rng()` (modern API) vs legacy `np.random` — the modern `Generator` API is preferred; it's statistically better and thread-safe
  ```python
  rng = np.random.default_rng(seed=42)  # create a seeded generator
  rng.integers(0, 10, size=5)           # array of 5 random ints in [0, 10)
  rng.normal(loc=0, scale=1, size=100)  # 100 standard normal samples

  # Legacy (avoid in new code):
  np.random.seed(42)
  np.random.randn(5)
  ```
- Seeds and reproducibility
- Distributions: `uniform`, `normal`, `poisson`, `choice`, `shuffle`, `permutation`
- `Generator` methods vs module-level functions
- Bootstrap sampling — resample with replacement to estimate statistics; each bootstrap sample is `rng.choice(data, size=len(data), replace=True)`

## Exercises

Implement the functions in `solution.py`.

### 1. `seeded_split(data, train_ratio, seed) -> tuple[np.ndarray, np.ndarray]`
Split data into train/test by ratio using the given seed. Must be reproducible.
```python
data = np.arange(10)
train, test = seeded_split(data, 0.8, seed=42)
len(train), len(test)  # (8, 2)
# Same seed always gives same split
```

### 2. `bootstrap_mean_ci(data, n_bootstrap, confidence, seed) -> tuple[float, float]`
Compute bootstrap confidence interval for the mean. Return (lower, upper).
```python
data = np.array([2, 4, 6, 8, 10], dtype=float)
lo, hi = bootstrap_mean_ci(data, n_bootstrap=10000, confidence=0.95, seed=42)
# lo ~ 3.2, hi ~ 8.8 (approximate)
```

### 3. `simulate_random_walk(n_steps, n_walks, seed) -> np.ndarray`
Simulate `n_walks` 1D random walks of `n_steps` each. Each step is +1 or -1 with equal probability. Return (n_walks, n_steps) cumulative sum array.
```python
walks = simulate_random_walk(100, 5, seed=42)
walks.shape  # (5, 100)
```

### 4. `weighted_sample_without_replacement(items, weights, k, seed) -> np.ndarray`
Sample k items without replacement according to weights. Use `rng.choice`.
```python
items = np.array(["a", "b", "c", "d", "e"])
weights = np.array([10, 1, 1, 1, 1])
weighted_sample_without_replacement(items, weights, 3, seed=42)
# 'a' should appear in most samples due to high weight
```
