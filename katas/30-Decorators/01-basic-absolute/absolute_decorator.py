# 1. make the code runnable by creating a decorator function 'absolute'
# 2. make the test running


@absolute
def foo(x):
    return 1 - x


assert foo(3) == 2