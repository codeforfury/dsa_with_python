# Problem Statement - Print Right aligned Right Angle Triangle pattern
# Author - Rajiv Das
# Date - 07-08-2026
# ----------------------------------------------------------
print("="*20)
print("Pattern 06".center(10, "-"))
print("="*20)

n = int(input("Enter the no. of line you want to print the pattern: "))
for i in range(1,n+1):
    for j in range(1,(n+1)-i):
        print(" ", end = "")
    
    for j in range(i):
        print("*", end="")
    print()

print("="*20)