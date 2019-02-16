"""
Decorating Examples.

from https://www.python-course.eu/python3_decorators.php.
"""
import sys
# from math import sin, cos
import math
import random
# from random import random, randint, choice


def one_parm_decorator(func):
    """Wrap given function f(x) in another, give that back (Decorating)."""
    def _function_wrapper(x):
        # We can decorate every other function which takes one parameter
        print("Before calling " + func.__name__)
        print(func(x))
        print("After calling " + func.__name__)
    return _function_wrapper


@one_parm_decorator  # semantically the same: myfunc=one_parm_decorator(myfunc)
def myfunc(n):
    """Sample function printing a string."""
    print("Hi, myfunc has been called with {}".format(n))
    return n + 1

# print("We now decorate myfunc with f:")
# Done with @one_parm_decorator instead now.
# myfunc = one_parm_decorator(myfunc)  # decorating style for imported modules


def my_func_test():
    """Test of one_parm_decorator with my_func(42)."""
    myfunc(42)


def one_parm_decorator_test():
    """Test of one_parm_decorator."""
    print("We call functions before decoration:")
    # myfunc(12)
    for f in [math.sin, math.cos]:
        res = f(1)
        # without one_parm_decorator there is no output here, so print it.
        print(res)

    # decorating style for imported modules
    sin = one_parm_decorator(math.sin)
    cos = one_parm_decorator(math.cos)
    print("We call functions after decoration:")
    # myfunc(42)
    for f in [sin, cos]:
        f(1)  # decoration one_parm_decorator prints the output for us.


def multi_parm_decorator(func):
    """Wrap given function f(x,y..) in another, give that back (Decorating)."""
    def _function_wrapper(*args, **kwargs):
        # We can decorate every function, regardless of how many parameters.
        print("Before calling " + func.__name__)
        res = func(*args, **kwargs)
        print(res)
        print("After calling " + func.__name__)
    return _function_wrapper


def multi_parm_decorator_test():
    """Test of multi_parm_decorator."""
    rand = multi_parm_decorator(random.random)
    randint = multi_parm_decorator(random.randint)
    choice = multi_parm_decorator(random.choice)

    rand()
    randint(3, 8)
    choice([4, 5, 6])


# The following program uses a decorator function to ensure that the argument
# passed to the function factorial is a positive integer:
def argument_test_natural_number(f):
    """Test whether a function got positive integer as parameter (Decor)."""
    def _helper(x):
        if isinstance(x, int) and x > 0:
            return f(x)
        else:
            raise Exception("Argument is not a positive integer")
    return _helper


@argument_test_natural_number
def factorial(n):
    """Factorial function: n * (n-1) * (n-2) * ... * 1 ."""
    if n == 1:
        return 1
    return n * factorial(n-1)


def argument_test_natural_number_sample():
    """Test of using decoration as a positive integer test."""
    for i in range(1, 10):
        print(i, factorial(i))

    print(factorial(-1))


def call_counter(func):
    """Decorate and store number of calls."""
    def _helper(x):
        _helper.calls += 1
        print("Num of calls, from inside _helper(x)", _helper.calls)
        return func(x)
    _helper.calls = 0
    # print("Num of calls, outside _helper, but in call_counter decorator",
    #       _helper.calls)
    return _helper


@call_counter
def succ(x):
    """Next Number."""
    print("Just counting inside succ():", x+1)
    return x + 1


def call_counter_test():
    """Print number of decorator calls."""
    print(succ.calls)
    for i in range(10):
        succ(i)

    print(succ.calls)


def greeting_with_decoration_parameter(expr):
    """Decorate with Parameters, to distinguish between morning and evening."""
    def _greeting_decorator(func):
        def _function_wrapper(x):
            print(expr + ", " + func.__name__ + " returns:")
            func(x)
        return _function_wrapper
    return _greeting_decorator


@greeting_with_decoration_parameter("καλημερα")
def print42(x):
    print(42)


def greeting_with_decoration_parameter_test():
    print42("Hi")  # Hi will be ignored later :-)


def main():
    """Choose Test (by uncommenting)."""
    # my_func_test()
    # one_parm_decorator_test()
    # multi_parm_decorator_test()
    # argument_test_natural_number_sample()
    # call_counter_test()
    greeting_with_decoration_parameter_test()
    return 0


if __name__ == "__main__":
    main()
