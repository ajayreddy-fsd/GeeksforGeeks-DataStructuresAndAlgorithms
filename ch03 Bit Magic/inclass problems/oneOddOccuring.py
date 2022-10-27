
# given an array, find the only number that appears odd number of times
def oneOddOccuring(arr):
    dict = {}
    for i in arr:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    for i in dict:
        if dict[i] % 2 != 0:
            return i


# the below reduces the auxiliary space
# xor of x even no. of times = 0
# xor of x odd no. of times = x
def efficient_oneOddOccuring(arr):
    result = 0  # since 0^A = A
    for i in arr:
        result ^= i
    return result


print(efficient_oneOddOccuring([4, 3, 4, 4, 4, 5, 5]))
print(efficient_oneOddOccuring([8, 7, 7, 8, 8]))
