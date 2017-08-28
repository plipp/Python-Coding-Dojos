# 1. make the code runnable by creating a decorator function 'absolute'
# 2. make the test running
from functools import wraps


def absolute(fn):
    @wraps(fn)
    def wrapper(*args, **kwarg):
        return abs(fn(*args, **kwarg))
    return wrapper

@absolute
def foo(x):
    return 1 - x


assert foo(3) == 2