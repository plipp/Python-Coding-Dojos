# 1. Make the test green (by completing the 'cache' implementation)
# 2. Enhance the TestCashDecorator: Check, that each decorated function has it's own cache-instance
from functools import wraps


def cache(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        # TODO lookup in/fill the cache
        return fn(*args, **kwargs)

    return wrapper


@cache
def fib(x):
    """Fibonacci series

    >>> fib(1)
    1
    >>> fib(2)
    2

    """
    if x < 0:
        raise ValueError('Must be greater than 0')
    elif x == 0:
        return 1
    elif x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


# ----------------------- the testing part

import unittest
from mock import Mock


class TestCashDecorator(unittest.TestCase):
    def test_cache_is_used(self):
        my_fn = Mock(name='my_fn')
        my_fn.return_value = 'hi'

        wrapped = cache(my_fn)
        # First call gives a call count of 1
        self.assertEqual(wrapped(3), 'hi')
        self.assertEqual(my_fn.call_count, 1)

        # Second call keeps the call count at 1 - the cached value is used
        self.assertEqual(wrapped(3), 'hi')
        self.assertEqual(my_fn.call_count, 1)

        # Subsequent call with a new value increased the call count
        self.assertEqual(wrapped(7), 'hi')
        self.assertEqual(my_fn.call_count, 2)


if __name__ == "__main__":
    unittest.main()
