class Solution:
    def exactly3Divisors(self,N):
        
        #checking for prime numbers less than root_N
        count = 0
        for i in range(2, int(N**0.5)+1):
            isPrime = True
            for j in range(2, int(i**0.5)+1):
                if i%j==0:
                    isPrime = False
                    break
            if isPrime:
                count+=1
                
        return count