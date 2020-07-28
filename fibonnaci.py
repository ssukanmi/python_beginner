"""
The popular fibonacci sequence
Constructed using different instructions
Measuring the time complexity for different ways of creating a fibonacci sequence
"""

import time


# getting the first n number of a fiboncci sequence
def first_n_while_fib(n):  # using a while loop
    lst = []

    if n == 1:
        lst = [0]
    elif n == 2:
        lst = [0, 1]
    else:
        lst = [0, 1]
        count = 2
        while count < n:
            lst.append(lst[-2] + lst[-1])
            count += 1
    return lst


def first_n_for_fib(n):  # using a for loop
    lst = []

    if n == 1:
        lst = [0]
    elif n == 2:
        lst = [0, 1]
    else:
        lst = [0, 1]
        for i in range(2, n):
            lst.append(lst[-2] + lst[-1])
    return lst


# finding the fibonacci sequence below the number x
def find_below_x_fib_while(x):  # using a while loop
    lst = [0, 1]
    while lst[-2] + lst[-1] < x:
        lst.append(lst[-2] + lst[-1])
    return lst

# using recurssion to find the nth term for a fibonacci sequence


# probably not the best solution cause the time complextiy increases exponentially
def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


start = time.time()
x = first_n_while_fib(30)
print(x)
print("it took {} secs using a while loop to execute".format(
    time.time() - start))

start = time.time()
y = first_n_for_fib(30)
print(y)
print("it took {} secs using a for loop to execute".format(
    time.time() - start))

z = find_below_x_fib_while(1000)
print(z)

start = time.time()
n = fibonacci_recursive(30)
print(n)
print("it took {} secs using python recurssion to execute".format(
    time.time() - start))
