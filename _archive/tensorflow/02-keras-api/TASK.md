# Task 2: Keras Sequential & Functional API

## Objective
Build models using both Keras APIs — understand when to use each, compile/fit/evaluate workflow.

## What to Learn
- `tf.keras.Sequential` for linear stacks
  ```python
  model = tf.keras.Sequential([
      tf.keras.Input(shape=(10,)),
      tf.keras.layers.Dense(64, activation="relu"),
      tf.keras.layers.Dense(3)
  ])
  ```
- Functional API: `tf.keras.Input`, layer chaining, `tf.keras.Model`
  ```python
  inp = tf.keras.Input(shape=(10,))
  x = tf.keras.layers.Dense(64, activation="relu")(inp)
  out = tf.keras.layers.Dense(3)(x)
  model = tf.keras.Model(inputs=inp, outputs=out)
  # Functional API required for multi-input/output or shared layers
  ```
- Common layers: `Dense`, `Dropout`, `BatchNormalization`
- `model.compile()`: optimizer, loss, metrics
  ```python
  model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
  ```
- `model.fit()`, `model.evaluate()`, `model.predict()`
- `model.summary()` and parameter counting

## Exercises

### 1. `build_sequential(in_features, out_features)`
Return a Sequential model: Input(in_features) -> Dense(64, relu) -> Dense(32, relu) -> Dense(out_features). Use `tf.keras.Input` as the first element.

```python
model = build_sequential(10, 3)
assert model.output_shape == (None, 3)
```

### 2. `build_functional(in_features, out_features)`
Same architecture using Functional API. Return the model.

```python
model = build_functional(10, 3)
assert model.output_shape == (None, 3)
assert len(model.inputs) == 1
```

### 3. `build_multi_input(num_features_a, num_features_b, out_features)`
Functional API model with two inputs. Each goes through Dense(32, relu), then concatenated, then Dense(16, relu) -> Dense(out_features).

```python
model = build_multi_input(5, 3, 2)
assert len(model.inputs) == 2
import numpy as np
a = np.random.randn(4, 5).astype("float32")
b = np.random.randn(4, 3).astype("float32")
out = model.predict([a, b], verbose=0)
assert out.shape == (4, 2)
```

### 4. `train_on_synthetic(n_epochs=20)`
Generate synthetic data (y = 2*x1 + 3*x2 + 1 + noise, 1000 samples). Build a Sequential model, compile with Adam and MSE. Fit with 20% validation split. Return a dict:
- `"history"`: the History object
- `"final_val_loss"`: last validation loss
- `"model"`: the trained model

```python
result = train_on_synthetic(50)
assert result["final_val_loss"] < 0.5
```
