def countDigits(n):
    if n == 0:
        return 1

    if n < 0:
        n = -n  # since // is floor-division operator, creates an infinite loop for negative numbers

    numDigits = 0

    while (n != 0):
        quotient = n//10
        numDigits += 1
        n = quotient

    return numDigits
