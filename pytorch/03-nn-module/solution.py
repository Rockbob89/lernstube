import torch
import torch.nn as nn


def build_sequential(in_features, out_features):
    pass


class TwoLayerNet(nn.Module):
    def __init__(self, in_features, hidden_features, out_features, dropout_p=0.5):
        super().__init__()
        pass

    def forward(self, x):
        pass


def count_parameters(model):
    pass


def freeze_layer(model, layer_name):
    pass


if __name__ == "__main__":
    # Exercise 1
    model = build_sequential(10, 3)
    print("Sequential output:", model(torch.randn(5, 10)).shape)

    # Exercise 2
    net = TwoLayerNet(784, 128, 10, dropout_p=0.3)
    print("TwoLayerNet output:", net(torch.randn(32, 784)).shape)

    # Exercise 3
    print("Parameters:", count_parameters(model))

    # Exercise 4
    print("Frozen:", freeze_layer(model, "0"))
