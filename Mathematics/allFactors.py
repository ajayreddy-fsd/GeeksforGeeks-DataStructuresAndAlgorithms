def allFactors(n):
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            print(i, int(n/i), end=", ")


def allFactorsCorrected(n):
    # suppose if a number is a perfect square, program prints it two times, so check and print only once
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            print(f'factor = {i}')
            if i != int(n/i):
                print(f'factor = {n//i}')


def allFactorsSorted(n):
    for i in range(1, int(n**0.5)):
        if n % i == 0:
            print(f'factor = {i}')
    for i in range(int(n**0.5), n+1):
        if n % i == 0:
            print(f'factor = {i}')


allFactorsSorted(56425)
