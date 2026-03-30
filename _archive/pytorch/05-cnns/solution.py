import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader


def calc_conv_output(input_size, kernel_size, stride=1, padding=0):
    pass


class SimpleCNN(nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()
        pass

    def forward(self, x):
        pass


def get_feature_maps(model, x):
    pass


def train_mnist(n_epochs=3):
    pass


if __name__ == "__main__":
    # Exercise 1
    print("Conv output:", calc_conv_output(28, 3, 1, 0))

    # Exercise 2
    model = SimpleCNN()
    x = torch.randn(8, 1, 28, 28)
    print("SimpleCNN output:", model(x).shape)

    # Exercise 3
    maps = get_feature_maps(model, torch.randn(1, 1, 28, 28))
    print("Feature maps:", [m.shape for m in maps])

    # Exercise 4 (uncomment to run — downloads data)
    # result = train_mnist(3)
    # print(f"Test accuracy: {result['test_acc']:.2%}")
