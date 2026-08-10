# Problem Statement - You are given an integer n. Return the integer formed by 
# placing the digits of n in reverse order.

# Author - Rajiv Das
# Date - 10-08-2026
# ----------------------------------------------------------

n = int(input("Enter a number:"))
sum = 0

while n > 0:  
    a = n % 10
    sum = (sum*10) + a
    n = n // 10
    
print("The number in reverse is:", sum)