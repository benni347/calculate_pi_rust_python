import profile
import time
import math
import timeit

N = 100_000_000


def factorial(n: int) -> int:
    """
    This is the method which will calculate it.
    :param n: the number to calculate the factorial of
    :return: the factorial of n
    """
    idx = 1
    x = 1
    while idx <= n:
        x = x * idx
        idx += 1
    print(x)
    return x


def sqrt(n: int) -> float | str:
    """
    Calculate the square root of n.
    :param n: the number to calculate the square root of
    :return: the square root of n
    """
    if n < 0:
        n *= -1
        return_value = str(n ** 0.5)
        # append an i to the end of the string
        return_value += "i"
    elif n == 0:
        return 0.0
    else:
        return_value = n ** 0.5
    return return_value


def ramanujan_algorithm(numerator: int) -> float:
    """
    Calculate pi to 15 decimal places using the Ramanujan algorithm.
    :return: pi as a float
    """
    sum_var = 0
    for i in range(0, numerator):
        n = factorial(4 * i) * (1103 + 26390 * i)
        denominator = factorial(i) ** 4 * (396 ** (4 * i))
        sum_var += n / denominator
        pi = (2 * sqrt(2) / 9801 * sum_var) ** -1
    return pi


def leibniz_formula(n_terms: int) -> float:
    """
    Calculate pi to 15 decimal places using the Leibniz formula.
    :source: https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
    :param n_terms: print for how many terms
    :return: pi to 15 decimal places as a float
    """
    numerator = 4.0
    denominator = 1.0
    operation = 1.0
    pi = 0.0
    for _ in range(n_terms):
        pi += operation * (numerator / denominator)
        denominator += 2.0
        operation *= -1.0
    return pi


if __name__ == "__main__":
    start_ramanujan = time.time()
    ramanujan = ramanujan_algorithm(15)
    print(f"ramanujan: {ramanujan} "
          f"time: {time.time() - start_ramanujan}")
    start_leibniz = time.time()
    leibniz = leibniz_formula(N)
    print(f"leibniz: {leibniz}:"
          f"time: {time.time() - start_leibniz}")