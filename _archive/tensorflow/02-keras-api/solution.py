import tensorflow as tf
import numpy as np


def build_sequential(in_features, out_features):
    pass


def build_functional(in_features, out_features):
    pass


def build_multi_input(num_features_a, num_features_b, out_features):
    pass


def train_on_synthetic(n_epochs=20):
    pass


if __name__ == "__main__":
    # Exercise 1
    model = build_sequential(10, 3)
    model.build((None, 10))
    print("Sequential summary:")
    model.summary()

    # Exercise 2
    model = build_functional(10, 3)
    print("\nFunctional summary:")
    model.summary()

    # Exercise 3
    model = build_multi_input(5, 3, 2)
    print("\nMulti-input summary:")
    model.summary()

    # Exercise 4
    result = train_on_synthetic(50)
    print(f"\nFinal val loss: {result['final_val_loss']:.4f}")
