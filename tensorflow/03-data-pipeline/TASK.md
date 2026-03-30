# Task 3: Data Pipeline

## Objective
Build efficient data pipelines with `tf.data.Dataset` — the standard way to feed data to TF models.

## What to Learn
- `tf.data.Dataset.from_tensor_slices()`
  ```python
  ds = tf.data.Dataset.from_tensor_slices((x_np, y_np))
  # Iterates as (single_x, single_y) pairs — batching happens next
  ```
- Transformations: `.map()`, `.batch()`, `.shuffle()`, `.prefetch()`
  ```python
  ds = (tf.data.Dataset.from_tensor_slices((x, y))
        .shuffle(buffer_size=1000)
        .map(augment_fn, num_parallel_calls=tf.data.AUTOTUNE)
        .batch(32)
        .prefetch(tf.data.AUTOTUNE))  # overlap GPU compute with CPU data prep
  ```
- `tf.data.AUTOTUNE` for optimal prefetching
- Writing and reading TFRecord files
  ```python
  # TFRecord: TF's binary format — efficient for large datasets on disk/GCS
  # Each record is a serialized tf.train.Example protobuf
  ```
- `tf.data.Dataset.from_generator()`
- Chaining transforms for train vs eval pipelines

## Exercises

### 1. `create_dataset(x, y, batch_size, shuffle=True)`
Create a `tf.data.Dataset` from numpy arrays `x` and `y`. If shuffle, shuffle with buffer size = len(x). Batch with given size. Prefetch with AUTOTUNE. Return the dataset.

```python
import numpy as np
x = np.random.randn(100, 5).astype("float32")
y = np.random.randint(0, 3, 100).astype("int32")
ds = create_dataset(x, y, batch_size=16)
for bx, by in ds.take(1):
    assert bx.shape == (16, 5)
    assert by.shape == (16,)
```

### 2. `augment_pipeline(ds, func)`
Take an existing dataset and apply a mapping function `func` to each element. Use `num_parallel_calls=tf.data.AUTOTUNE`. Return the new dataset.

```python
def double_x(x, y):
    return x * 2, y
ds2 = augment_pipeline(ds, double_x)
```

### 3. `write_tfrecord(data, labels, path)` and `read_tfrecord(path, feature_dim)`
Write float features and int labels to a TFRecord file. Read them back. Each record stores `"features"` as FloatList and `"label"` as Int64List.

```python
x = np.random.randn(50, 3).astype("float32")
y = np.array([0, 1] * 25, dtype="int64")
write_tfrecord(x, y, "/tmp/data.tfrecord")
ds = read_tfrecord("/tmp/data.tfrecord", feature_dim=3)
for features, label in ds.take(1):
    assert features.shape == (3,)
```

### 4. `build_train_val_pipeline(x, y, batch_size=32, val_split=0.2)`
Split data into train/val. Training pipeline: shuffle + batch + prefetch. Validation pipeline: batch + prefetch (no shuffle). Return `(train_ds, val_ds)`.

```python
x = np.random.randn(200, 5).astype("float32")
y = np.random.randint(0, 2, 200).astype("int32")
train_ds, val_ds = build_train_val_pipeline(x, y)
```
