import math
def quadraticRoots(self, a, b, c):
    delta = b*b - 4*a*c
    if delta == 0:
        return [math.floor(-b/(2*a))]*2
    elif delta > 0:
        root1 = math.floor((-b+(delta**0.5))/(2*a))
        root2 = math.floor((-b-(delta**0.5))/(2*a))
        return [max(root1, root2), min(root1, root2)]
    else:
        return [-1]

