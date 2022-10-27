import math
class Solution:
    
    #Function to find the first position with different bits.
    def posOfRightMostDiffBit(self,m,n):
        #Your code here
        num = m^n
        if num == 0:
            return -1
        return int(math.log(num & (~(num-1)), 2)+1)