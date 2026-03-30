import os
import tensorflow as tf
import numpy as np


def save_and_load_keras(model, path):
    pass


def export_savedmodel(model, path):
    pass


def convert_to_tflite(model, path):
    pass


def add_serving_signature(model, path):
    pass


if __name__ == "__main__":
    # Build a simple model for testing
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(32, activation="relu", input_shape=(10,)),
        tf.keras.layers.Dense(3),
    ])
    model.compile(optimizer="adam", loss="mse")

    # Exercise 1
    loaded = save_and_load_keras(model, "/tmp/model.keras")
    print("Loaded model:", loaded)

    # Exercise 2
    result = export_savedmodel(model, "/tmp/saved_model")
    print("SavedModel contents:", result["contents"])

    # Exercise 3
    result = convert_to_tflite(model, "/tmp/model.tflite")
    print(f"TFLite size: {result['size_kb']:.1f} KB")

    # Exercise 4
    keys = add_serving_signature(model, "/tmp/serving_model")
    print("Signature keys:", keys)
