# Task 5: CNNs

## Objective
Build convolutional neural networks — understand conv layers, pooling, feature maps, and how to wire a CNN for image classification.

## What to Learn
- `nn.Conv2d`: in_channels, out_channels, kernel_size, stride, padding
  ```python
  nn.Conv2d(1, 16, kernel_size=3, padding=1)
  # 1 input channel (grayscale), 16 feature maps, 3x3 kernel
  # padding=1 keeps spatial size: (28-3+2)/1+1 = 28
  ```
- `nn.MaxPool2d`, `nn.AdaptiveAvgPool2d`
  ```python
  nn.MaxPool2d(2)              # halves spatial dims: 28x28 → 14x14
  nn.AdaptiveAvgPool2d((1,1))  # any input size → 1x1 output (global average)
  ```
- `nn.BatchNorm2d`
  ```python
  nn.BatchNorm2d(16)  # normalizes each of the 16 channels across the batch
  # Speeds training and reduces sensitivity to weight init; place after Conv, before activation
  ```
- Output size calculation: `(W - K + 2P) / S + 1`
- Flattening conv output for fully-connected layers
  ```python
  x = conv_block(x)        # shape: (batch, 32, 7, 7)
  x = x.view(x.size(0), -1)  # shape: (batch, 32*7*7=1568)
  ```
- MNIST/FashionMNIST with `torchvision.datasets`

## Exercises

### 1. `calc_conv_output(input_size, kernel_size, stride=1, padding=0)`
Return the output spatial dimension after a conv/pool operation.

```python
assert calc_conv_output(28, 3, 1, 0) == 26
assert calc_conv_output(28, 5, 1, 2) == 28
assert calc_conv_output(28, 3, 2, 1) == 14
```

### 2. Class `SimpleCNN(nn.Module)`
Build a CNN for 1-channel 28x28 images (MNIST-like):
- Conv2d(1, 16, 3, padding=1) -> BN -> ReLU -> MaxPool(2)
- Conv2d(16, 32, 3, padding=1) -> BN -> ReLU -> MaxPool(2)
- Flatten -> Linear(32*7*7, 128) -> ReLU -> Dropout(0.5) -> Linear(128, num_classes)

Constructor takes `num_classes=10`.

```python
model = SimpleCNN()
x = torch.randn(8, 1, 28, 28)
out = model(x)
assert out.shape == (8, 10)
```

### 3. `get_feature_maps(model, x)`
Pass input `x` through only the conv layers (up to flatten). Return the intermediate feature maps as a list of tensors (one per conv block).

```python
model = SimpleCNN()
x = torch.randn(1, 1, 28, 28)
maps = get_feature_maps(model, x)
assert len(maps) == 2
assert maps[0].shape == (1, 16, 14, 14)
assert maps[1].shape == (1, 32, 7, 7)
```

### 4. `train_mnist(n_epochs=3)`
Download FashionMNIST, train SimpleCNN for `n_epochs`. Return a dict:
- `"train_acc"`: final training accuracy
- `"test_acc"`: test accuracy (should reach >80% in 3 epochs)
- `"model"`: the trained model

```python
result = train_mnist(3)
print(f"Test accuracy: {result['test_acc']:.2%}")
```
