# Problem Statement - You are given an integer n. You need to check whether the 
# number is a palindrome number or not. Return true if it's a palindrome 
# number, otherwise return false. A palindrome number is a number which reads the 
# same both left to right and right to left.

# Author - Rajiv Das
# Date - 10-08-2026
# ----------------------------------------------------------

n = int(input("Enter a number"))
duplicate = n
rev = 0

while n > 0:  
    a = n % 10
    rev = (rev*10) + a
    n = n// 10
    
if rev == duplicate:
    print("The number is Palindrome")
else:
    print("The number is not Palindrome")