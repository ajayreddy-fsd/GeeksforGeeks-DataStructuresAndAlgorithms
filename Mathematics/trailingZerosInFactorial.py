from nFactorial import nFactorial
import math


def trailingZerosInFactorial(n):
    num = nFactorial(n)
    count = 0

    remainder = num % 10
    while remainder == 0:
        count += 1
        num = num//10
        remainder = num % 10
    return count


def efficient_trailingZerosInFactorial(n):
    count = 0
    i = 1

    while n//(5**i) != 0:
        count += n//(5**i)
        i += 1
    return count


