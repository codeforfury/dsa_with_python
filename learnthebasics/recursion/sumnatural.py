# Sum of first N Natural Numbers

# Problem Statement - Given a number ‘N’, find out the sum of the first N natural numbers .
# Author - Rajiv Das
# Date - 23-08-2026
# ----------------------------------------------------------

# Three ways to do this - 
# 1) Brute Force approach i.e. using loop from 1 to N [takes O(n) time complexity]
# 2) Recursion approach which we will do now [takes O(n) time complexity]
# 3) Optimal approach i.e. using formula - n(n+1)/2 [takes O(1) time complexity] will do this also. 


# 2) Recursion approach - 
'''
def sumnatural(n):
    if n < 1:
        return 0
    
    return n + sumnatural(n - 1)

print(sumnatural(5))'''


# 3) Optimal approach - 
n = 5
sum = n*(n + 1)//2
print(sum)