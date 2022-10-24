from cmath import nan


def nFactorial(n):
    if n < 0:
        return 'NaN'
    elif n == 0:
        return 1
    else:
        return n * nFactorial(n-1)

