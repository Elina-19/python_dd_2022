def find_max(*args):
    maximum = args[0]

    for arg in args:
        if arg > maximum:
            maximum = arg

    return maximum


print(find_max(5, 3, 8, 10, 3))
