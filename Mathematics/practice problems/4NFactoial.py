class Solution:
    #You need to complete this function
    def factorial(self,N):
        #Your code here
        result = 1
        for i in range(1,N+1):
            result *= i
        return result