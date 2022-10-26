def allPrimesLessThanN(n):
    arr = [True]*(n+1)

    for i in range(2, len(arr)):
        if arr[i]:
            print(i, end=' ')

            j = i*i
            # why not start from i+i,
            # coz mulitples of numbers which are less than i,
            # have already made composite numbers less than i^2 False
            while j < n+1:
                arr[j] = False
                j += i


allPrimesLessThanN(1000)
