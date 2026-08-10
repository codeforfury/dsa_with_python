# Problem Statement - You are given an integer n. You need to check if the 
# number is prime or not. Return true if it is a prime number, otherwise return 
# false. A prime number is a number which has no divisors except 1 and itself.

# Author - Rajiv Das
# Date - 11-08-2026
# ----------------------------------------------------------

# 1)Brute Force approach - We can iterate through numbers from 1 to n, 
# counting how many of these numbers divide n without a remainder. 
# If exactly two numbers do, so n is prime otherwise it is not prime.
'''
n = 10
count = 0

for i in range(1, n+1):
    if n % i == 0:
        count += 1

if count == 2:
    print("Prime")
else:
    print("Not Prime")'''


# 2)Optimal approach - A number's factors occur in complementary pairs (i, n/i), 
# so it is sufficient to check divisors only up to √n. 
# For each divisor found, count both i and n/i (if distinct); 
# if the total number of factors is exactly 2, 
# the number is prime, otherwise it is composite.

n = 97
count = 0

for i in range(1, int(n**0.5)+1):
    if n % i == 0:
        count += 1
        
        if i != (n // i):
            count += 1  

if count == 2:
    print("Prime")
else:
    print("Not Prime")