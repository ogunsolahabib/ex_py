# https://exercism.org/tracks/python/exercises/flatten-array

def flatten(iterable):
    stack =[]
    for x in iterable:
        if isinstance(x, list):
            stack.extend(flatten(x))
        elif isinstance(x, int):
            stack.append(x)
    return stack
