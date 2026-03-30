# Task 3: nn.Module

## Objective
Build neural networks using `torch.nn.Module` — understand layers, forward pass, parameter management, and model structure.

## What to Learn
- Subclassing `nn.Module`: `__init__()` and `forward()`
  ```python
  class MyNet(nn.Module):
      def __init__(self):
          super().__init__()
          self.fc = nn.Linear(10, 5)  # must assign layers as attributes
      def forward(self, x):
          return torch.relu(self.fc(x))  # called by model(x), not model.forward(x)
  ```
- Common layers: `nn.Linear`, `nn.ReLU`, `nn.Sigmoid`, `nn.Dropout`
- `model.parameters()` and `model.named_parameters()`
  ```python
  for name, param in model.named_parameters():
      print(name, param.shape)  # e.g. "fc.weight" torch.Size([5, 10])
  ```
- `nn.Sequential` for simple stacks
  ```python
  model = nn.Sequential(nn.Linear(10, 64), nn.ReLU(), nn.Linear(64, 5))
  # model(x) runs layers in order; no custom forward() needed
  ```
- Input/output dimensions and how they flow through layers

## Exercises

### 1. `build_sequential(in_features, out_features)`
Return an `nn.Sequential` model: Linear(in, 64) -> ReLU -> Linear(64, 32) -> ReLU -> Linear(32, out).

```python
model = build_sequential(10, 3)
x = torch.randn(5, 10)
out = model(x)
assert out.shape == (5, 3)
```

### 2. Class `TwoLayerNet(nn.Module)`
Build a custom module: Linear(in, hidden) -> ReLU -> Dropout(p) -> Linear(hidden, out). Constructor takes `in_features`, `hidden_features`, `out_features`, `dropout_p=0.5`.

```python
net = TwoLayerNet(784, 128, 10, dropout_p=0.3)
x = torch.randn(32, 784)
out = net(x)
assert out.shape == (32, 10)
```

### 3. `count_parameters(model)`
Return the total number of trainable parameters in a model.

```python
model = build_sequential(10, 3)
# Linear(10,64): 10*64+64=704, Linear(64,32): 64*32+32=2080, Linear(32,3): 32*3+3=99
assert count_parameters(model) == 2883
```

### 4. `freeze_layer(model, layer_name)`
Set `requires_grad=False` for all parameters in the named layer. Return the number of parameters frozen.

```python
model = build_sequential(10, 3)
frozen = freeze_layer(model, "0")  # first Linear
assert frozen == 704
# Verify frozen
for p in model[0].parameters():
    assert p.requires_grad is False
```
