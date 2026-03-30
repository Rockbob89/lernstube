from functools import wraps


def validate_types(**type_kwargs):
    pass


if __name__ == "__main__":
    @validate_types(name=str, age=int)
    def register(name, age):
        return f"{name} is {age}"

    print(register(name="Alice", age=30))  # → Alice is 30

    try:
        register(name="Alice", age="thirty")
    except TypeError as e:
        print(e)  # → Expected age to be <class 'int'>, got <class 'str'>
