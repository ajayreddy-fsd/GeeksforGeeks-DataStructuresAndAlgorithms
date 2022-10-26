def HCFOfTwoNumbers(a, b):
    a = abs(a)
    b = abs(b)

    if a == 0:
        return b
    if b == 0:
        return a

    big = max(a, b)
    small = min(a, b)

    return HCFOfTwoNumbers(small, big % small)


