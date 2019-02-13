#!/usr/bin/python3
""".
from: https://stackabuse.com/python-nested-functions/
We can bind/pass data to a function without necessarily passing the data to the function via parameters. This is done using a closure. It is a function object that is able to remember values in the enclosing scopes even when they are not available in the memory. This means that we have a closure when a nested function references a value that is in its enclosing scope.

The purpose of a closure is to make the inner function remember the state of its environment when it is called, even if it is not in the memory. A closure is caused by an inner function, but it's not the inner function. The closure works by closing the local variable on the stack, which stays around after the creation of the stack has finished executing.

    * There must be a nested function
    * The inner function has to refer to a value that is defined in the enclosing scope
    * The enclosing function has to return the nested function
"""


def function1(name):

    def function2():
        print('Hello ' + name)  # inner func refers to outer 'name' variable
    return function2  # enclosing (outer) function returns nested (inner).


func = function1('Simon')
print(func)  # <function function1.<locals>.function2 at 0x7fcebe9a3620>
func()  # closing the local variable on the stack

""".
The above code demonstrates that ''with closures, we are able to generate and invoke a function from outside its scope via function passing''. The scope of function2() is only inside function1(). However, with the use of closures, it was possible for us to extend this scope and invoke it from outside its scope.

''Inner functions help us in defining factory functions. A factory function is a function that creates another object.'' For example:
"""


def power_generator(num):

    # Create the inner function: factory function
    # since it generates functions for us using the parameter we pass it.
    def power_n(power):
        return num ** power  # ref to outer variable 'num'

    return power_n  # return inner function from outer

power_two = power_generator(2)
power_three = power_generator(3)

print(power_two)
print(power_three)
# result:
# <function power_generator.<locals>.power_n at 0x7faecb31c9d8>
# <function power_generator.<locals>.power_n at 0x7faecb31ca60>

print(power_two(8))
print(power_three(4))
