# Print name N times using recursion

# Problem Statement: Given an integer N, write a program to print your name N times.

# Author - Rajiv Das
# Date - 22-08-2026
# ----------------------------------------------------------

def func(count, n):
    if count == n:
        return
    
    print("Rajiv")
    func(count + 1, n)

n = int(input("Enter how many times you want to print:"))
func(1, n+1)