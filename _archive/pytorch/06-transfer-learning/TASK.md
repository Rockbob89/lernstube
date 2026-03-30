# Task 6: Transfer Learning

## Objective
Use pretrained models from torchvision, adapt them to new tasks via fine-tuning and feature extraction.

## What to Learn
- `torchvision.models` and pretrained weights (e.g., ResNet18)
  ```python
  from torchvision.models import resnet18, ResNet18_Weights
  model = resnet18(weights=ResNet18_Weights.IMAGENET1K_V1)
  ```
- Replacing the final classification head
  ```python
  model.fc = nn.Linear(model.fc.in_features, num_classes)
  # ResNet18's fc is the only layer that changes — rest stays pretrained
  ```
- Freezing backbone layers vs fine-tuning all layers
  ```python
  for param in model.parameters():
      param.requires_grad = False   # freeze everything
  for param in model.fc.parameters():
      param.requires_grad = True    # unfreeze only the head
  ```
- Learning rate strategies: lower LR for pretrained layers
- `torchvision.transforms` for input preprocessing

## Exercises

### 1. `load_pretrained_resnet(num_classes)`
Load ResNet18 with pretrained weights. Replace the final `fc` layer to output `num_classes`. Freeze all layers except the new `fc`. Return the model.

```python
model = load_pretrained_resnet(5)
x = torch.randn(2, 3, 224, 224)
out = model(x)
assert out.shape == (2, 5)
# Only fc should be trainable
trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
total = sum(p.numel() for p in model.parameters())
assert trainable < total * 0.01  # fc is tiny vs full model
```

### 2. `unfreeze_last_n_layers(model, n)`
Unfreeze the last `n` children of the model (excluding the fc which is already unfrozen). Return count of newly unfrozen parameters.

```python
model = load_pretrained_resnet(5)
unfrozen = unfreeze_last_n_layers(model, 2)
print(f"Unfroze {unfrozen} parameters")
```

### 3. `get_param_groups(model, backbone_lr, head_lr)`
Return a list of param group dicts suitable for `torch.optim.Adam`. Two groups: backbone params with `backbone_lr`, head (fc) params with `head_lr`.

```python
groups = get_param_groups(model, 1e-5, 1e-3)
assert len(groups) == 2
optimizer = torch.optim.Adam(groups)
```

### 4. `get_transforms(train=True)`
Return torchvision transforms for ResNet input. Training: Resize(256) -> RandomCrop(224) -> RandomHorizontalFlip -> ToTensor -> Normalize(ImageNet stats). Eval: Resize(256) -> CenterCrop(224) -> ToTensor -> Normalize.

```python
train_t = get_transforms(train=True)
eval_t = get_transforms(train=False)
```
