import math
# finds where the first set bot is located from right
# if no set bits, returns zero


def firstSetBit(n):
    if n == 0:
        return 0
    return int(math.log(n & (~(n-1)), 2)+1)


print(firstSetBit(65280))
