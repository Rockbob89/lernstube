import torch


def manual_gradient(x_val):
    pass


def gradient_accumulation():
    pass


def no_grad_demo(x_val):
    pass


def detach_demo(x_val):
    pass


if __name__ == "__main__":
    print("manual_gradient(2.0):", manual_gradient(2.0))
    print("manual_gradient(0.0):", manual_gradient(0.0))
    print("gradient_accumulation():", gradient_accumulation())
    print("no_grad_demo(5.0):", no_grad_demo(5.0))
    print("detach_demo(3.0):", detach_demo(3.0))
