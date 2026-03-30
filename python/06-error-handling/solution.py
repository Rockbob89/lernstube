class AppError(Exception):
    pass

class ValidationError(AppError):
    pass

class NotFoundError(AppError):
    pass

def safe_divide(a, b):
    pass

def parse_config(data, required_keys):
    pass


if __name__ == "__main__":
    # exceptions
    try:
        raise ValidationError("email", "must contain @")
    except ValidationError as e:
        print(e)

    try:
        raise NotFoundError("User", 42)
    except NotFoundError as e:
        print(e)

    # safe_divide
    print(safe_divide(10, 3))
    print(safe_divide(10, 0))
    print(safe_divide("a", 3))

    # parse_config
    try:
        parse_config({"host": "localhost"}, ["host", "port"])
    except ValidationError as e:
        print(e)
        print(f"caused by: {e.__cause__}")
