import torch
import numpy as np


def create_tensors():
    pass


def tensor_ops(a, b):
    pass


def reshape_drill(x):
    pass


def numpy_roundtrip(np_array):
    pass


if __name__ == "__main__":
    # Exercise 1
    result = create_tensors()
    print("create_tensors:", {k: v.shape for k, v in result.items()})

    # Exercise 2
    a = torch.tensor([1.0, 2.0, 3.0])
    b = torch.tensor([4.0, 5.0, 6.0])
    print("tensor_ops:", tensor_ops(a, b))

    # Exercise 3
    x = torch.arange(24, dtype=torch.float32)
    print("reshape_drill:", {k: v.shape for k, v in reshape_drill(x).items()})

    # Exercise 4
    arr = np.array([1.0, 2.0, 3.0])
    print("numpy_roundtrip:", numpy_roundtrip(arr))
