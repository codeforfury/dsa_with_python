# Problem Statement - Print Inverted 1 to N Right Angle Triangle pattern
# Author - Rajiv Das
# Date - 07-08-2026
# ----------------------------------------------------------
print("="*20)
print("Pattern 05".center(10, "-"))
print("="*20)

n = int(input("Enter the no. of line you want to print the pattern: "))
for i in range(n,0,-1):
    for j in range(i):
        print(j+1, end = "")
    print()

print("="*20)