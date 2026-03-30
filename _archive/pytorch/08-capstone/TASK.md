# Task 8: Capstone — Image Classifier

## Objective
Build an end-to-end image classification pipeline: data loading, augmentation, model training (with transfer learning), evaluation, and export.

## Requirements

### Dataset
Use FashionMNIST or CIFAR-10 (your choice). Split into train/validation/test.

### Model
- Use transfer learning (ResNet18 or similar)
- For FashionMNIST: convert grayscale to 3-channel
- Replace classification head for your dataset's classes

### Training
- Proper training loop with validation monitoring
- Learning rate scheduling (e.g., `StepLR` or `ReduceLROnPlateau`)
- Early stopping based on validation loss
- Data augmentation during training
- Log training/validation loss and accuracy per epoch

### Evaluation
- Test set accuracy, precision, recall per class
- Confusion matrix (print or plot)

### Export
- Save best model as TorchScript
- Provide a `predict(image_path)` function that loads the saved model and classifies a single image

### Deliverables
- `solution.py` — all code
- Printed summary: final metrics, training time, model size
- Target: >85% test accuracy

No stub provided. Build from scratch using everything from tasks 1-7.
