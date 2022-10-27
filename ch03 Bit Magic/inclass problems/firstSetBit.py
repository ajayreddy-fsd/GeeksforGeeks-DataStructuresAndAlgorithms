
# finds where the first set bot is located from right
# if no set bits, returns zero
def firstSetBit(n):
    return n & (~(n-1))


print(firstSetBit(0))
