# 1. Make the test green (by completing the 'cache' implementation)
# 2. Enhance the TestCashDecorator: Check, that each decorated function has it's own cache-instance
from functools import wraps





def cache(fn):
    CACHE = dict()
    @wraps(fn)
    def wrapper(n):
        if n not in CACHE:
            CACHE[n] = fn(n)
        return CACHE[n]

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
from unittest.mock import Mock


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

    def test_cache_is_local(self):
        my_fn1 = Mock(name='my_fn1')
        my_fn1.return_value = 'hi1'

        my_fn2 = Mock(name='my_fn2')
        my_fn2.return_value = 'hi2'

        wrapped1 = cache(my_fn1)
        wrapped2 = cache(my_fn2)

        self.assertEqual(wrapped1(4), 'hi1')

        self.assertEqual(wrapped2(4), 'hi2')


if __name__ == "__main__":
    unittest.main()
