

lookUpTable = {0: 0}


# generates look up table for all 8-bit numbers
def generateLookUpTable():
    for i in range(1, 2**8):

        # storing the value of i,
        # as its value changes after entering the loop
        num = i
        count = 0
        while (i != 0):
            i = i & (i-1)
            count += 1
        lookUpTable[num] = count


generateLookUpTable()
print(lookUpTable)
