# Problem Statement - Given a digit d (0 to 9), find the sum of the first 50 
# positive integers (integers > 0) that end with digit d. 
# A number ends with digit d if its last digit is d.

# Author - Rajiv Das
# Date - 09-08-2026
# ----------------------------------------------------------

d = int(input("Enter the number to represent digit d: "))
total = 0

while d < 0 or d > 9:
    print("Invalid input!")
    d = int(input("Enter a digit from 0 to 9: "))
    
for i in range(50):
    total = total + d
    d = d + 10

print(total)