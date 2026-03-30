import tensorflow as tf
import numpy as np


def create_dataset(x, y, batch_size, shuffle=True):
    pass


def augment_pipeline(ds, func):
    pass


def write_tfrecord(data, labels, path):
    pass


def read_tfrecord(path, feature_dim):
    pass


def build_train_val_pipeline(x, y, batch_size=32, val_split=0.2):
    pass


if __name__ == "__main__":
    x = np.random.randn(100, 5).astype("float32")
    y = np.random.randint(0, 3, 100).astype("int32")

    # Exercise 1
    ds = create_dataset(x, y, batch_size=16)
    for bx, by in ds.take(1):
        print("Batch shapes:", bx.shape, by.shape)

    # Exercise 2
    ds2 = augment_pipeline(ds, lambda x, y: (x * 2, y))
    for bx, by in ds2.take(1):
        print("Augmented batch:", bx.shape)

    # Exercise 3
    x3 = np.random.randn(50, 3).astype("float32")
    y3 = np.array([0, 1] * 25, dtype="int64")
    write_tfrecord(x3, y3, "/tmp/data.tfrecord")
    ds3 = read_tfrecord("/tmp/data.tfrecord", feature_dim=3)
    for feat, label in ds3.take(1):
        print("TFRecord sample:", feat.shape, label)

    # Exercise 4
    train_ds, val_ds = build_train_val_pipeline(x, y)
    print("Train/val pipelines created")
