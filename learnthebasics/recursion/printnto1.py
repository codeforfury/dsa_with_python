# Print N to 1 using Recursion

# Problem Statement: Given an integer N, write a program to print numbers from N to 1.

# Author - Rajiv Das
# Date - 22-08-2026
# ----------------------------------------------------------

# For this prg also we have 2 method i.e. forward and backtracking. 

# For for now we will do the forward method only

def back(n):
    if n < 1:
        return
    
    print(n)
    back(n-1)

back(5)
