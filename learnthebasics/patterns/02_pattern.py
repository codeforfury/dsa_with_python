# Problem Statement - Print 1 to N Right Angle Triangle pattern
# Author - Rajiv Das
# Date - 07-08-2026
# ----------------------------------------------------------
print("="*20)
print("Pattern 02".center(10, "-"))
print("="*20)

n = int(input("Enter the no. of line you want to print the pattern: "))
for i in range(n):
    for j in range(i+1):
        print(j+1, end = "")
    print()

print("="*20)