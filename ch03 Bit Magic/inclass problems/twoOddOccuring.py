# given an array, find the only two numbers that appear odd number of times
import math
def twoOddOccuring(arr):
    result = 0
    for i in arr:
        result ^= i

    # k gives the position of first set bit from right
    # if k=1, then the first bit from right in result is 1
    # if k=2, then the second bit from right in result is 1
    # if k = 0, then no set bits in result
    # k = 0 can never ocuur coz there are definitely 2 odd occurrences in the given array
    k = int(math.log(result & (~(result-1)), 2)+1)
    num1 = 0
    num2 = 0

    # divide the elements based on this set bit
    for i in arr:
        if i >> (k-1) & 1:
            num1 ^= i
        else:
            num2 ^= i

    return [num1, num2]


print(twoOddOccuring([1, 3, 2, 3, 3, 1]))
