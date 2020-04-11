import functools
import logging
import time


logging.basicConfig(level=logging.DEBUG)


def timed(func):
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        args = [repr(arg_) for arg_ in args]
        kwargs = [fr'{k}={v}' for k, v in kwargs.items()]
        signature = ','.join(args + kwargs)
        msg = f'{func.__name__}({signature}) finished in {elapsed} sec'
        logging.debug(msg)
        return res
    return wrapped_func


# Stateful Decorators --------------------------------------------------------
def count_calls(func):
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        wrapped_func.num_calls += 1
        msg = f'Call {wrapped_func.num_calls} time(s) of {func.__name__}'
        logging.debug(msg)
        return func(*args, **kwargs)
    wrapped_func.num_calls = 0
    return wrapped_func


# Example:
# @memoize(maxsize=5)
# def fib(n):
#     if n == 0 or n == 1:
#         return 1
#     return fib(n - 1) + fib(n - 2)
def memoize(maxsize: int = 10):
    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            compound_key = args + tuple(kwargs.items())
            if compound_key in inner.cached:
                return inner.cached[compound_key]
            else:
                res = func(*args, **kwargs)
                if len(inner.cached) <= maxsize:
                    inner.cached[compound_key] = res
                return res
        inner.cached = dict()
        return inner
    return outer
