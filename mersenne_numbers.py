"""
A Mersenne number is any number that can be written as  (2^p - 1) for some  p 
For example, 3 is a Mersenne number (2^2 - 1) as is 31 (2^5 − 1)
We will see later on that it is easy to test if Mersenne numbers are prime.
"""


def mersenne_number(p):
    return 2**p - 1


def is_prime(n):  # finding out if a number is prime or not
    if n < 2:
        return False
    for factor in range(2, n//2 + 1):
        if n % factor == 0:
            return False
    return True


def get_prime(n_start, n_end):  # get all the primes between n_start and n_end prime numbers
    x = []
    for number in range(n_start, n_end+1):
        if is_prime(number):
            x.append(mersenne_number(number))
    return x


# a list of the Mersenne numbers for all primes (p) between 3 and 65
print(get_prime(3, 65))
