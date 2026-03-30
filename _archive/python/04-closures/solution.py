def counter():
    pass


def make_multiplier(factor):
    pass


if __name__ == "__main__":
    # counter
    c = counter()
    print(c(), c(), c())  # → 1 2 3

    # make_multiplier
    double = make_multiplier(2)
    triple = make_multiplier(3)
    print(double(5))   # → 10
    print(triple(5))   # → 15
