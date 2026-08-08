# Problem Statement - Given two integers low and high, return the sum of all 
# integers from low to high inclusive.

# Author - Rajiv Das
# Date - 09-08-2026
# ----------------------------------------------------------

sum = 0
low = int(input("Enter the lower range for sum initiation"))
high = int(input("Enter the highest range for sum"))

for i in range(low, high+1):
    sum = sum + i

print(sum)