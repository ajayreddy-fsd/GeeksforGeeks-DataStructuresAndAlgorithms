
# Kth bit is the bit from last
def KthBitSetOrNot(n, k):
    if n == 0:
        return False

    iterations = 0
    while n != 0:
        iterations += 1
        bit = n % 2
        n = n//2
        if iterations == k:
            if bit == 1:
                return True
            else:
                break
    return False


# using right-shift operator
def efficient_KthBitSetOrNot_1(n, k):
    return True if (n >> (k-1)) & 1 == 1 else False


# using left-shift operator
def efficient_KthBitSetOrNot_2(n, k):
    return True if (1 << (k-1)) & 1 != 0 else False
