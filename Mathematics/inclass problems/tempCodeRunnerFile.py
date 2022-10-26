def efficientPrimeFactorization(n):
#     for i in range(2, n+1):
#         temp = 1 #variable to track of all prime factors by multiplying them with one another
#         if checkPrime(i) and n % i == 0:
#             print(i, end=' ')
#             temp *= i

#             #check if i^2, i^3, ... also divide n
#             x = i**2
#             while (n % x == 0):
#                 print(i, end=' ')
#                 temp *= i
#                 x = x*i
        
#         n = n//temp