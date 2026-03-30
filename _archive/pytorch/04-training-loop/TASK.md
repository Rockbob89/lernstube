# Task 4: Training Loop

## Objective
Implement a complete training loop from scratch — loss computation, backprop, optimizer step, and data loading with `DataLoader`.

## What to Learn
- Loss functions: `nn.CrossEntropyLoss`, `nn.MSELoss`
- Optimizers: `torch.optim.SGD`, `torch.optim.Adam`
- The train step: zero_grad -> forward -> loss -> backward -> step
  ```python
  optimizer.zero_grad()      # clear old gradients
  pred = model(x)            # forward pass
  loss = loss_fn(pred, y)    # compute loss
  loss.backward()            # compute gradients
  optimizer.step()           # update weights
  ```
- `torch.utils.data.Dataset` and `DataLoader`
  ```python
  class MyDataset(Dataset):
      def __len__(self): return len(self.data)
      def __getitem__(self, idx): return self.data[idx], self.labels[idx]

  loader = DataLoader(MyDataset(), batch_size=32, shuffle=True)
  ```
- `model.train()` vs `model.eval()` modes
  ```python
  model.train()  # enables Dropout, BatchNorm uses batch stats
  model.eval()   # disables Dropout, BatchNorm uses running stats
  ```
- Basic validation loop

## Exercises

### 1. Class `SyntheticDataset(Dataset)`
Create a dataset that generates `n_samples` points from `y = 2x + 1 + noise`. Constructor takes `n_samples` and `noise_std=0.1`. Implements `__len__` and `__getitem__` returning `(x_tensor, y_tensor)` where both are 1D tensors of shape `(1,)`.

```python
ds = SyntheticDataset(100)
x, y = ds[0]
assert x.shape == (1,) and y.shape == (1,)
assert len(ds) == 100
```

### 2. `train_one_epoch(model, dataloader, loss_fn, optimizer)`
Run one epoch of training. Return the average loss for the epoch as a float.

```python
model = nn.Linear(1, 1)
ds = SyntheticDataset(200)
loader = DataLoader(ds, batch_size=32, shuffle=True)
loss_fn = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
avg_loss = train_one_epoch(model, loader, loss_fn, optimizer)
print(avg_loss)  # some float
```

### 3. `evaluate(model, dataloader, loss_fn)`
Run evaluation (no gradient computation). Return average loss as float.

```python
avg_loss = evaluate(model, loader, loss_fn)
```

### 4. `train_linear_regression(n_epochs=50)`
Put it all together. Create dataset (500 train, 100 val), model, optimizer (Adam, lr=0.01), loss (MSE). Train for `n_epochs`. Return a dict:
- `"final_train_loss"`: float
- `"final_val_loss"`: float
- `"weight"`: learned weight (should be close to 2.0)
- `"bias"`: learned bias (should be close to 1.0)

```python
result = train_linear_regression(100)
assert abs(result["weight"] - 2.0) < 0.2
assert abs(result["bias"] - 1.0) < 0.2
```
