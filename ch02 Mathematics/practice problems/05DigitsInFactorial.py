import math
class Solution:
    def digitsInFactorial(self,N):
        # code here
        if N==1:
            return 1
        
        logValue = 0
        for i in range(2, N+1):
            logValue += math.log10(i)
            
        return math.ceil(logValue)
        