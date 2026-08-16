# Linear Search.

# Problem Statement - Given an array, and an element num the task is to 
# find if num is present in the given array or not. If present print the 
# index of the element or print -1.
# Time complexity - O(n)
# Space Complexity - O(1)

# Author - Rajiv Das
# Date - 16-08-2026
# ----------------------------------------------------------

arr = [5,8,2,3,7,1,20,10]
num = 20
for i in range(len(arr)):
    if arr[i] == num:
        print(i)
        break

else:
    print(-1)