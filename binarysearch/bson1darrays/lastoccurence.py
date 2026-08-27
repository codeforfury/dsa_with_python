# Last occurrence in a sorted array.

# Problem Statement - Given a sorted array of N integers, write a program to 
# find the index of the last occurrence of the target key. If the target 
# is not found then return -1. Note: Consider 0 based indexing

# Author - Rajiv Das
# Date - 26-08-2026
# ----------------------------------------------------------

# Two approaches for doing this - 

# 1) Brute Force Approach - Traverse the sorted array from right to left. 
# If nums[i] == target, return i immediately because the first match 
# encountered is the last occurrence. If no match is found, return -1.
# Time: O(n)
# Space: O(1)

# 2) Optimal Approach - Use binary search on the sorted array. 
# When nums[mid] == x, store mid and continue searching the right 
# half to find a later occurrence. If nums[mid] < x, move right; 
# otherwise, move left. If no occurrence is found, return -1.
# Time: O(log n)
# Space: O(1)


# 1) Brute Force Approach -
'''
nums = [3, 4, 13, 13, 13, 20, 40]
x = 13

for i in range(len(nums)-1, -1,-1):
    if nums[i] == x:
        print("The index of last occurence is:", i)
        break

else:
    print("The element is not present")'''


# 2) Optimal Approach -

nums = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12, 13, 13, 13, 13, 40]
x = 12
index = -1
low = 0
high = len(nums) - 1

while(low <= high):
    mid = (low + high) // 2

    if nums[mid] == x:
        index = mid
        low = mid + 1

    elif nums[mid] < x:
        low = mid + 1

    else:
        high = mid - 1

if index == -1:
    print("The element is not present")
else:
    print("The index of last occurence is:", index)