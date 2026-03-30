import tensorflow as tf


def create_tensors():
    pass


def tensor_ops(a, b):
    pass


def gradient_tape_demo(x_val):
    pass


def tf_function_demo():
    pass


if __name__ == "__main__":
    # Exercise 1
    result = create_tensors()
    print("create_tensors:", {k: v.shape for k, v in result.items()})

    # Exercise 2
    a = tf.constant([1.0, 2.0, 3.0])
    b = tf.constant([4.0, 5.0, 6.0])
    print("tensor_ops:", tensor_ops(a, b))

    # Exercise 3
    print("gradient_tape_demo(2.0):", gradient_tape_demo(2.0))
    print("gradient_tape_demo(0.0):", gradient_tape_demo(0.0))

    # Exercise 4
    print("tf_function_demo:", tf_function_demo())
