import os
import tempfile
import torch
import torch.nn as nn


def save_and_load_model(model, path):
    pass


def export_torchscript(model, example_input, path):
    pass


def export_onnx(model, example_input, path):
    pass


def compare_formats(model, example_input):
    pass


if __name__ == "__main__":
    model = nn.Linear(10, 3)
    x = torch.randn(1, 10)

    # Exercise 1
    loaded = save_and_load_model(model, "/tmp/model.pt")
    print("Loaded model:", loaded)

    # Exercise 2
    scripted = export_torchscript(model, x, "/tmp/model_ts.pt")
    print("TorchScript output:", scripted(x).shape)

    # Exercise 3
    export_onnx(model, x, "/tmp/model.onnx")
    print("ONNX exported")

    # Exercise 4
    print("Format sizes:", compare_formats(model, x))
