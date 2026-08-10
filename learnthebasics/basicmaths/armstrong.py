# Problem Statement - You are given an integer n. You need to check whether it is 
# an armstrong number or not. Return true if it is an armstrong number, otherwise 
# return false. An armstrong number is a number which is equal to the sum of the 
# digits of the number, raised to the power of the number of digits.

# Author - Rajiv Das
# Date - 11-08-2026
# ----------------------------------------------------------

n = int(input("Enter a number"))
save = n
original = n
count = 0
sum = 0

while n > 0:
    count += 1
    n = n // 10

while save > 0:
    a = save % 10
    sum = sum + a**count
    save = save // 10

if original == sum:
    print("Armstrong")
else:
    print("Not Armstrong")