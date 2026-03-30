# Task 5: Saving & Serving

## Objective
Save models in TensorFlow formats, convert for edge deployment, and understand TF Serving basics.

## What to Learn
- `model.save()` / `tf.keras.models.load_model()` (Keras format)
  ```python
  model.save("model.keras")                         # Keras v3 format
  loaded = tf.keras.models.load_model("model.keras")
  ```
- SavedModel format and its directory structure
  ```
  saved_model/
  ├── saved_model.pb      # graph definition and signatures
  ├── variables/          # weights (checkpoint)
  └── assets/             # optional: vocab files, etc.
  ```
- TFLite conversion: `tf.lite.TFLiteConverter`
  ```python
  converter = tf.lite.TFLiteConverter.from_keras_model(model)
  tflite_model = converter.convert()  # quantize optionally for edge deployment
  ```
- Signatures and serving functions
  ```python
  # Signatures define the named input/output contract for TF Serving
  # Default key is "serving_default"
  ```
- TF Serving container basics (conceptual)

## Exercises

### 1. `save_and_load_keras(model, path)`
Save model in Keras format (`.keras`). Load it back. Verify predictions match on random input. Return the loaded model.

```python
model = build_simple_cnn(10)  # from task 4
loaded = save_and_load_keras(model, "/tmp/model.keras")
```

### 2. `export_savedmodel(model, path)`
Export as SavedModel. List the directory contents. Return a dict:
- `"path"`: the export path
- `"contents"`: list of files/dirs in the saved model directory

```python
result = export_savedmodel(model, "/tmp/saved_model")
print(result["contents"])  # ['assets', 'saved_model.pb', 'variables']
```

### 3. `convert_to_tflite(model, path)`
Convert a Keras model to TFLite. Save to `path`. Load back with `tf.lite.Interpreter` and run inference on a random input. Return a dict:
- `"size_kb"`: model size in KB
- `"output_shape"`: output shape from interpreter

```python
result = convert_to_tflite(model, "/tmp/model.tflite")
print(f"TFLite size: {result['size_kb']:.1f} KB")
```

### 4. `add_serving_signature(model, path)`
Export SavedModel with an explicit serving signature. The signature should accept a named input tensor and return a named output. Return the signature keys.

```python
keys = add_serving_signature(model, "/tmp/serving_model")
print(keys)  # e.g., ['serving_default']
```
