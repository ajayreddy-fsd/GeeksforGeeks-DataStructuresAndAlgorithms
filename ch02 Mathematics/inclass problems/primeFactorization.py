from checkPrime import checkPrime
import math


def primeFactorization(n):
    for i in range(2, n+1):
        if checkPrime(i) and n % i == 0:
            print(i, end=' ')

            # check if i^2, i^3, ... also divide n
            x = i**2
            while (n % x == 0):
                print(i, end=' ')
                x = x*i


def efficientPrimeFactorization(n):

    while (n % 2 == 0):
        print(f'primeFactor = 2')
        n = n//2

    while (n % 3 == 0):
        print(f'primeFactor = 3')
        n = n//3

    for i in range(5, math.floor(n**0.5)+1):
        while (n % i == 0):
            print(f'primeFactor = {i}')
            n = n//i

        while (n % (i+2) == 0):
            print(f'primeFactor = {i+2}')
            n = n//(i+2)

    if n>3:
        print(f'primeFactor = {n}')

efficientPrimeFactorization(450)
