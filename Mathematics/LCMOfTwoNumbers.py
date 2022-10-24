from re import L
from HCFOfTwoNumbers import HCFOfTwoNumbers

def LCMOfTwoNumbers(a, b):
    return abs(a*b)//HCFOfTwoNumbers(a,b)

print(LCMOfTwoNumbers(20, 30))

