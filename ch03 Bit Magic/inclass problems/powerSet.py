# returns powerSet of a given set
# s is a string
def powerSet(s):
    powerSet = ['']

    n = len(s)
    for i in range(1, 2**n):

        powerSetElement = ''
        iteration = 0
        while (i != 0):
            powerSetElement += s[iteration] * (i % 2)
            i = i//2
            iteration += 1
        powerSet.append(powerSetElement)

    return powerSet

print(powerSet('abcdef'))