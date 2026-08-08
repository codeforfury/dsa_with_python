# Problem Statement - Print Inverted Right aligned 54321 5432 543 to 5 Right Angle Triangle pattern
# Author - Rajiv Das
# Date - 08-08-2026
# ----------------------------------------------------------
print("="*20)
print("Pattern 10".center(10, "-"))
print("="*20)

n = int(input("Enter the no. of line you want to print the pattern: "))
for i in range(1,(n+1)):
    for j in range(1,i):
        print(" ", end = "")
    
    for j in range(n,i-1,-1):
        print(j, end="")
    print()

print("="*20)