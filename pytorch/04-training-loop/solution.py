import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader


class SyntheticDataset(Dataset):
    def __init__(self, n_samples, noise_std=0.1):
        pass

    def __len__(self):
        pass

    def __getitem__(self, idx):
        pass


def train_one_epoch(model, dataloader, loss_fn, optimizer):
    pass


def evaluate(model, dataloader, loss_fn):
    pass


def train_linear_regression(n_epochs=50):
    pass


if __name__ == "__main__":
    # Exercise 1
    ds = SyntheticDataset(100)
    print("Dataset length:", len(ds))
    print("Sample:", ds[0])

    # Exercise 2 & 3
    model = nn.Linear(1, 1)
    loader = DataLoader(ds, batch_size=32, shuffle=True)
    loss_fn = nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
    print("Train loss:", train_one_epoch(model, loader, loss_fn, optimizer))
    print("Eval loss:", evaluate(model, loader, loss_fn))

    # Exercise 4
    result = train_linear_regression(100)
    print("Final result:", result)
