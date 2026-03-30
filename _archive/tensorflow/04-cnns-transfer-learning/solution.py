import tensorflow as tf
import numpy as np


def build_simple_cnn(num_classes=10):
    pass


def build_transfer_model(num_classes, input_shape=(224, 224, 3)):
    pass


def unfreeze_top_layers(model, n):
    pass


def get_callbacks(patience=5, checkpoint_path="/tmp/best_model.keras"):
    pass


if __name__ == "__main__":
    # Exercise 1
    model = build_simple_cnn(10)
    print("SimpleCNN output:", model.predict(np.random.randn(4, 28, 28, 1).astype("float32"), verbose=0).shape)

    # Exercise 2
    model = build_transfer_model(5)
    model.summary(show_trainable=True)

    # Exercise 3
    model = unfreeze_top_layers(model, 20)
    print("After unfreezing:")
    trainable = sum(1 for l in model.layers if l.trainable)
    print(f"Trainable layers: {trainable}")

    # Exercise 4
    callbacks = get_callbacks()
    print("Callbacks:", [type(cb).__name__ for cb in callbacks])
