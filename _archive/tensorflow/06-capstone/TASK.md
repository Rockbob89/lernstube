# Task 6: Capstone — Model Pipeline

## Objective
Build an end-to-end ML pipeline: data loading with `tf.data`, training with transfer learning, evaluation, and export as SavedModel.

## Requirements

### Dataset
Use FashionMNIST or CIFAR-10 via `tf.keras.datasets`. Split into train/validation/test.

### Data Pipeline
- Build with `tf.data.Dataset`
- Training: shuffle, augmentation (random flip, slight rotation), batch, prefetch
- Validation/test: batch, prefetch (no augmentation)

### Model
- Transfer learning with MobileNetV2 or similar
- For grayscale datasets: resize and convert to 3 channels
- Custom classification head with dropout

### Training
- Callbacks: EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
- Two-phase training: train head only, then fine-tune top layers
- Track and print metrics per epoch

### Evaluation
- Test accuracy, per-class precision/recall
- Confusion matrix (print or plot)

### Export
- Save as SavedModel with serving signature
- Convert to TFLite and compare sizes
- Provide a `predict(image_array)` function using the SavedModel

### Deliverables
- `solution.py` — all code
- Printed summary: final metrics, training time, model sizes
- Target: >85% test accuracy

No stub provided. Build from scratch using everything from tasks 1-5.
