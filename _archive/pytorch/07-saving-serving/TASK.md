# Task 7: Saving & Serving

## Objective
Save and load models for inference, export to portable formats (TorchScript, ONNX).

## What to Learn
- `torch.save()` / `torch.load()` with `state_dict`
  ```python
  torch.save(model.state_dict(), "model.pt")   # saves weights only
  model.load_state_dict(torch.load("model.pt")) # requires same architecture defined first
  ```
- Why save state_dict vs the whole model
  ```
  Saving the whole model with torch.save(model, ...) pickles the class definition.
  state_dict is just a dict of tensors — portable across refactors and Python versions.
  ```
- TorchScript: `torch.jit.trace()` and `torch.jit.script()`
  ```python
  traced = torch.jit.trace(model, example_input)   # records ops for that input shape
  scripted = torch.jit.script(model)                # compiles the forward() source
  traced.save("model_ts.pt")  # deployable without Python
  ```
- ONNX export: `torch.onnx.export()`
  ```python
  torch.onnx.export(model, example_input, "model.onnx",
                    dynamic_axes={"input": {0: "batch"}})  # batch dim flexible
  ```
- Model versioning considerations

## Exercises

### 1. `save_and_load_model(model, path)`
Save the model's state_dict to `path`. Create a new instance of the same architecture. Load the state_dict. Return the loaded model. Verify outputs match on a random input.

```python
model = build_sequential(10, 3)  # from task 3
save_and_load_model(model, "/tmp/model.pt")
```

### 2. `export_torchscript(model, example_input, path)`
Export model via `torch.jit.trace`. Save to `path`. Load it back and verify output matches. Return the loaded scripted model.

```python
model = nn.Linear(10, 3)
scripted = export_torchscript(model, torch.randn(1, 10), "/tmp/model_ts.pt")
out = scripted(torch.randn(1, 10))
assert out.shape == (1, 3)
```

### 3. `export_onnx(model, example_input, path)`
Export model to ONNX format. Use dynamic axes for batch dimension. Return the path.

```python
export_onnx(nn.Linear(10, 3), torch.randn(1, 10), "/tmp/model.onnx")
```

### 4. `compare_formats(model, example_input)`
Save the same model in all three formats (state_dict, TorchScript, ONNX) to a temp directory. Return a dict with file sizes in bytes for each format.

```python
model = nn.Linear(10, 3)
sizes = compare_formats(model, torch.randn(1, 10))
print(sizes)  # {"state_dict": ..., "torchscript": ..., "onnx": ...}
```
