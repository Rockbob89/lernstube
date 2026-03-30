# Task 4: CNNs & Transfer Learning

## Objective
Build CNNs in Keras and apply transfer learning with pretrained models from `tf.keras.applications`.

## What to Learn
- `Conv2D`, `MaxPooling2D`, `BatchNormalization`, `Flatten`, `GlobalAveragePooling2D`
  ```python
  x = tf.keras.layers.Conv2D(16, 3, padding="same", activation="relu")(inp)
  x = tf.keras.layers.MaxPooling2D(2)(x)    # halves spatial dims
  x = tf.keras.layers.GlobalAveragePooling2D()(x)  # (batch, H, W, C) → (batch, C)
  ```
- Pretrained models: `MobileNetV2`, `ResNet50`, `EfficientNetB0`
- `include_top=False` for feature extraction
  ```python
  base = tf.keras.applications.MobileNetV2(include_top=False, weights="imagenet",
                                           input_shape=(224, 224, 3))
  base.trainable = False  # freeze the backbone
  x = tf.keras.layers.GlobalAveragePooling2D()(base.output)
  out = tf.keras.layers.Dense(num_classes, activation="softmax")(x)
  model = tf.keras.Model(base.input, out)
  ```
- Freezing/unfreezing layers
- Fine-tuning strategies
- `tf.keras.callbacks`: EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
  ```python
  tf.keras.callbacks.EarlyStopping(monitor="val_loss", patience=5, restore_best_weights=True)
  tf.keras.callbacks.ReduceLROnPlateau(factor=0.5, patience=3)
  ```

## Exercises

### 1. Class `SimpleCNN` (via Functional API)
Build: Input(28,28,1) -> Conv2D(16,3,padding='same') -> BN -> ReLU -> MaxPool(2) -> Conv2D(32,3,padding='same') -> BN -> ReLU -> MaxPool(2) -> Flatten -> Dense(128,relu) -> Dropout(0.5) -> Dense(num_classes). Return as a function `build_simple_cnn(num_classes=10)`.

```python
model = build_simple_cnn(10)
assert model.output_shape == (None, 10)
out = model.predict(np.random.randn(4, 28, 28, 1).astype("float32"), verbose=0)
assert out.shape == (4, 10)
```

### 2. `build_transfer_model(num_classes, input_shape=(224, 224, 3))`
Load MobileNetV2 with `include_top=False`, `weights="imagenet"`. Freeze it. Add GlobalAveragePooling2D -> Dense(128, relu) -> Dropout(0.3) -> Dense(num_classes, softmax). Return the model.

```python
model = build_transfer_model(5)
trainable = sum(1 for l in model.layers if l.trainable)
frozen = sum(1 for l in model.layers if not l.trainable)
print(f"Trainable layers: {trainable}, Frozen: {frozen}")
```

### 3. `unfreeze_top_layers(model, n)`
Unfreeze the last `n` layers of the base model inside a transfer model. The model must be ready for fine-tuning after this call. Return the model.

```python
model = build_transfer_model(5)
model = unfreeze_top_layers(model, 20)
```

### 4. `get_callbacks(patience=5, checkpoint_path="/tmp/best_model.keras")`
Return a list of callbacks: EarlyStopping (monitor val_loss, patience, restore_best_weights), ModelCheckpoint (save_best_only), ReduceLROnPlateau (factor=0.5, patience=3).

```python
callbacks = get_callbacks()
assert len(callbacks) == 3
```
