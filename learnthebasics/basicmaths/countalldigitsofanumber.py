# Problem Statement - You are given an integer n. You need to return the 
# number of digits in the number.

# Author - Rajiv Das
# Date - 10-08-2026
# ----------------------------------------------------------

n = int(input("Enter a number"))
c = 0

while n > 0:  #this approach takes O(log base10 N + 1) time complexity
    c += 1
    n = n//10

print("The number of digit:",c)