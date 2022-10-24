from checkPrime import checkPrime

def f(n):
    arr = [True]*n

    for i in range(2,n+1):
        if n%i == 0:
            arr[i] = False

    for i in arr:
        if i:
            print(i, end=' ')
f(100)