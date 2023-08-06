# permutation, combination, print_fac, print_*, n'th fib

import ctypes as c
import os
import sys

if sys.platform.startswith('darwin'):
    _ = c.CDLL(os.path.join(os.path.dirname(__file__), "gmp.dylib"))

if sys.platform.startswith('cygwin') or sys.platform.startswith('win32'):
    _ = c.CDLL(os.path.join(os.path.dirname(__file__), "gmp.dll"))


_.pfib.argtypes = (c.c_ulonglong,)

_.factorial.argtypes = (c.c_ulong,)
_.factorial.restype = c.c_char_p

_.fibonacci.argtypes = (c.c_ulong, c.c_ulong)
_.fibonacci.restype = c.c_char_p


def print_fib(term_count: int):
    '''prints fibonacci series up to the term_count'''

    if not (isinstance(term_count, int) and term_count > 0):
        raise ValueError("'term_count' has to be bigger than 0 and 'int'.")

    _.pfib(term_count)


def factorial(term: int) -> int:
    '''prints the factorial of `term`.'''

    if not (isinstance(term, int) and term >= 0):
        raise ValueError("'term' has to be bigger than 0 and 'int'.")

    return int(_.factorial(term).decode('utf-8'))


def fibonacci(term: int, precision: int = 1000) -> int:
    '''prints the term'th term of the fibonacci serie.'''

    if not (isinstance(term, int) and term >= 0):
        raise ValueError("'term' has to be bigger than 0 and 'int'.")

    return int(_.fibonacci(term, precision).decode('utf-8'))


if __name__ == "__main__":
    pass
