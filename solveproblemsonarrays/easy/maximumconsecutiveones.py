# Count Maximum Consecutive One's in the array

# Problem Statement - Given an array that contains only 1 and 0 return the count 
# of maximum consecutive ones in the array.
# Time complexity - O(n)
# Space Complexity - O(1)

# Author - Rajiv Das
# Date - 16-08-2026
# ----------------------------------------------------------

arr = [1,0,1,0,0,1,1,0,1]
c = 0
maximum = 0
for i in arr:
    if i == 1:
        c += 1
        maximum = max(maximum, c)
    else:
        c = 0

print("Max no. of one's:", maximum)