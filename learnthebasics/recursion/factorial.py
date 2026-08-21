# Factorial of a given number

# Problem Statement: Given a number X,  print its factorial.

# Author - Rajiv Das
# Date - 21-08-2026
# ----------------------------------------------------------

# There are two approaches - 

# Iterative Solution - This we already know i.e multiply all of those looping from 1 to N. 
# Recursive Solution - We will do this now.

# Recursive approach

def fact(n):
    if n < 1:
        return 1
    
    return n * fact(n - 1)

print(fact(5))