# Problem Statement - You are given an integer n. You need to find all the 
# divisors of n. Return all the divisors of n as an array or list in a sorted 
# order. A number which completely divides another number is called it's divisor.

# Author - Rajiv Das
# Date - 11-08-2026
# ----------------------------------------------------------

#1) The brute force approach to find all the divisors of a number is to iterate through 
# every number from 1 to N and check whether it is a divisor or not.
'''
n = 36
for i in range(1, n+1):
    if n % i == 0:
        print(i)'''


#2) Optimal approach - Divisors of a number always occur in pairs (d, N/d). 
# Therefore, it is sufficient to check divisors only up to √N; 
# whenever a divisor is found, its corresponding pair is obtained using N/d, 
# reducing the time complexity from O(N) to O(√N).

import math

n = 36

for i in range(1, int(math.sqrt(n))+1):
    if n % i == 0:
        print(i)

        if i != n// i:
            print(n // i)