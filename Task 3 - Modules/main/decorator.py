def decorator(func):
    def wrapper(*args, **kwargs):
        print("arguments: ", args)
        result = func(*args, **kwargs)
        print("result: ", result)

        return result
    return wrapper


@decorator
def find_max(*args):
    maximum = args[0]

    for arg in args:
        if arg > maximum:
            maximum = arg

    return maximum


find_max(5, 3, 8, 10, 3)
