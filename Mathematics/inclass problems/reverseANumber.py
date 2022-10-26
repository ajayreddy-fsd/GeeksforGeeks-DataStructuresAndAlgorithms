from countDigits import countDigits


def reverseANumber(n):
    revNum = 0
    numDigits = countDigits(n)
    isNegative = False

    if numDigits == 1:
        return n

    if n < 0:
        isNegative = True
        n = -n

    for i in range(numDigits):
        lastDigit = n % 10
        revNum += lastDigit * (10 ** (countDigits(n)-1))
        n = n//10

    if (isNegative):
        return -revNum
    else:
        return revNum
