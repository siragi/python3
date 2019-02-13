#!/usr/bin/python3
""".
The code returns the multiplication of the two numbers, that is, 10 and 5. The example shows that an inner function is able to access variables accessible in the outer function.
"""


def num1(x):
    def num2(y):
        return x * y
    return num2


# result variable is defined as a function (but the result of it can not be determined yet, because the function is not complete.)
res = num1(10)
print(res)  # result: <function num1.<locals>.num2 at 0x7f40a51d6620>

# the result variable (incomplete function) takes another variable
print(res(5))

# -----------------------------------------------------------------------
""".
The output shows that it is possible for us to display the value of a variable defined within the outer function from the inner function, but not change it. The statement x = 6 helped us create a new variable x inside the inner function function2() rather than changing the value of variable x defined in the outer function function1().
"""


def function1():  # outer function
    x = 2  # A variable defined within the outer function

    def function2(a):  # inner function
        # Let's define a new variable within the inner function
        # rather than changing the value of x of the outer function
        x = 6
        print(a+x)
    print(x)  # to display the value of x of the outer function
    function2(3)


function1()
# 2
# 9

# -----------------------------------------------------------------
""".
Encapsulation.
A function can be created as an inner function in order to protect it from everything that is happening outside of the function. In that case, the function will be hidden from the global scope.
"""


def outer_function(x):
    # Hidden from the outer code

    def inner_increment(x):
        return x + 2
    y = inner_increment(x)
    print(x, y)


# inner_increment(5):  #NameError: name 'inner_increment' is not defined
outer_function(5)
