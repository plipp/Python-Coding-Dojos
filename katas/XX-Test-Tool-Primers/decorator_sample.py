# --------------- 1. Explicit Logging


def info(msg):
    print("INFO - {}".format(msg))


# some business logic with logging

def do_something1(n):
    info("do_something1 called with: n={}".format(n))
    return n + 1


# --------------- 2 a) Logging with self-made decorator

def with_logging1(fun):
    def wrapper(*args, **kwargs):
        info("{} called with : {},{}".format(fun.__name__, args, kwargs))
        return fun(*args, **kwargs)

    return wrapper


# -- hand-made

def do_something2(n):
    return n + 2


do_something2 = with_logging1(do_something2)


# -- with @

@with_logging1  # just a short way of saying: do_something3 = with_logging(do_something3)
def do_something3(n):
    """
    some docstring for do_something3
    :param n: number
    :return: n + 3
    """
    return n + 3


# --------------- 2 b) Logging with self-made decorator, complete

def with_logging2(fun):
    def wrapper(*args, **kwargs):
        info("{} called with : {},{}".format(fun.__name__, args, kwargs))
        return fun(*args, **kwargs)

    wrapper.__name__ = fun.__name__
    wrapper.__doc__ = fun.__doc__
    return wrapper


@with_logging2
def do_something4(n):
    """
    some docstring for do_something4
    :param n: number
    :return: n + 4
    """
    return n + 4


# --------------- 2 c) Logging with decorator and functools-support

from functools import wraps


def with_logging3(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        info("{} called with : {},{}".format(fun.__name__, args, kwargs))
        return fun(*args, **kwargs)

    return wrapper


@with_logging3
def do_something5(n):
    """
    some docstring for do_something5
    :param n: number
    :return: n + 5
    """
    return n + 5


# -------------------------------------------------------------------

if __name__ == '__main__':
    print('{} 1. Explicit Logging\n'.format('-' * 20))

    print(do_something1(4))

    # print('{} 2 a) Logging with self-made decorator\n'.format('-' * 20))
    #
    # print(do_something2(4))
    # print(do_something3(n=4))
    #
    # print("do_something3.__name__: {}".format(do_something3.__name__))
    # print("do_something3.__doc__ : {}".format(do_something3.__doc__))
    #
    # print('{} 2 b) Logging with self-made decorator, complete\n'.format('-' * 20))
    #
    # print(do_something4(n=4))
    # print("do_something4.__name__: {}".format(do_something4.__name__))
    # print("do_something4.__doc__ : {}".format(do_something4.__doc__))
    #
    # print('{} 2 c) Logging with decorator and functools-support\n'.format('-' * 20))
    #
    # print(do_something5(4))
    # print("do_something5.__name__: {}".format(do_something5.__name__))
    # print("do_something5.__doc__ : {}".format(do_something5.__doc__))


# ... further reading
# - http://book.pythontips.com/en/testing/decorators.html
# - http://jamescooke.info/things-to-remember-about-decorators.html
