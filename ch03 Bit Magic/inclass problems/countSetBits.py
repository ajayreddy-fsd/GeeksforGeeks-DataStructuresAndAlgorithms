#n is non-negative
def countSetBits(n):
    if n == 0:
        return 0

    count = 0
    while n != 0:
        bit = n % 2
        n = n//2
        if bit:
            count += 1
    return count


# using BK algorithm
def efficient_countSetBits(n):
    if n == 0:
        return 0

    count = 0
    while n != 0:
        # whenever u do n-1,
        # all the trailing zeros become ones
        # and the first set bit from right becomes zero
        n = n & (n-1)
        count += 1
    return count
