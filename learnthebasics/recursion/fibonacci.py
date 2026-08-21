# Print Fibonacci Series up to Nth term.

# Problem Statement: Given an integer N. Print the Fibonacci series up to the Nth term.

# Author - Rajiv Das
# Date - 21-08-2026
# ----------------------------------------------------------

# Three ways of doing it - 

# 1) Brute Force Approach - using Array storing first 2 elements as 0 and 1 then summing 
# last two digits continuing till N. O(n) time and O(n) space complexity.

# 2) Recursion Approach - we will do this now. O(2^N) time and O(n) space complexity.

# 3) Optimal Approach - Just using simple loops. O(n) time and O(1) space complexity.


#2) Recursion Approach -
'''
def fib(N):
    if N <= 1:
        return N

    return fib(N - 1) + fib(N - 2)

n = 0
for i in range(n):
    print(fib(i), end=" ")
'''

# 3) Optimal Approach - 

n = 5
if n <= 0:
    pass
elif n == 1:
    print(0)
else:
    sl = 0
    l = 1

    print(0, 1, end=" ")

    for i in range(3, n + 1):
        curr = sl + l
        print(curr, end=" ")
        sl = l
        l = curr