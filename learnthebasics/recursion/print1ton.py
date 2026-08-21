# Print 1 to N using Recursion.

# Problem Statement: Given an integer N, write a program to print numbers from 1 to N.

# Author - Rajiv Das
# Date - 21-08-2026
# ----------------------------------------------------------

# First method - Forward Recursion it prints the current number and then 
# recursively calls itself with the next number incremented by one.
'''
def forward(i, n):
    if i == n:
        return
    
    print(i)
    forward(i + 1, n)

n = int(input("Enter the highest term till you want to print:"))
forward(1, n + 1)'''


# Second method - Backtracking To print numbers from 1 to n using backtracking, 
# the function recursively calls itself with the next number until it passes n. 
# After reaching the base case, it prints the numbers while returning from the recursion. 
# This way, numbers are printed in reverse order because the print happens after 
# the recursive call during backtracking. The main difference from forward recursion is 
# that printing occurs on the way back, not before the recursive call.

def forward(i, n):
    if i == n:
        return
    
    forward(i + 1, n)
    print(i)

n = int(input("Enter the highest term till you want to print:"))
forward(1, n + 1)