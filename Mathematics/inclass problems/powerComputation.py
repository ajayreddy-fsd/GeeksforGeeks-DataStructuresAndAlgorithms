# TC reduced from O(n) to O(logn), but got an auxiliary space of theta(logn)

import math


def powerComputation(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    if n == 2:
        return x*x
    if n % 2 == 0:
        return powerComputation(x, n//2) * powerComputation(x, n//2)
    else:
        return powerComputation(x, n//2) * powerComputation(x, n//2) * x


def efficientPowerComputation(x, n):
    if n == 0:
        return 1

    result = 1
    multiplier = x

    # decomposing n into binary
    while n != 0:
        if n % 2 == 1:
            result *= multiplier
        multiplier *= multiplier
        n = n//2

    return result
