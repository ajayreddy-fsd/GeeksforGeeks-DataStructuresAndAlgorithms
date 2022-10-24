from countDigits import countDigits


def palindrome(n):
    if n < 0:
        n = -n  # just a precaution, as // is floor-division-operator

    if n == 0:
        return True

    while n != 0:
        numDigits = countDigits(n)
        firstDigit = n//(10 ** (numDigits-1))
        lastDigit = n % 10

        if firstDigit != lastDigit:
            return False

        n = (n//10) % (10**(numDigits-2))
    return True




