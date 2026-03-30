import torch
import torch.nn as nn
import torchvision
import torchvision.models as models
import torchvision.transforms as transforms


def load_pretrained_resnet(num_classes):
    pass


def unfreeze_last_n_layers(model, n):
    pass


def get_param_groups(model, backbone_lr, head_lr):
    pass


def get_transforms(train=True):
    pass


if __name__ == "__main__":
    # Exercise 1
    model = load_pretrained_resnet(5)
    print("Output shape:", model(torch.randn(2, 3, 224, 224)).shape)
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    total = sum(p.numel() for p in model.parameters())
    print(f"Trainable: {trainable}/{total}")

    # Exercise 2
    print("Unfrozen:", unfreeze_last_n_layers(model, 2))

    # Exercise 3
    groups = get_param_groups(model, 1e-5, 1e-3)
    print("Param groups:", len(groups))

    # Exercise 4
    print("Train transforms:", get_transforms(train=True))
    print("Eval transforms:", get_transforms(train=False))
