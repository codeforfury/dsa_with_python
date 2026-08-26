# Search Element in a Rotated Sorted Array.

# Problem Statement - Given a rotated sorted array of distinct integers and a 
# target value x, find the index of x in the array. If x is not 
# present, return -1. The array was originally sorted in ascending 
# order but has been rotated at an unknown pivot.

# Author - Rajiv Das
# Date - 26-08-2026
# ----------------------------------------------------------

# Two approaches for doing this - 

# 1) Brute Force Approach - Traverse the array from left to right and 
# compare each element with the target x. If nums[i] == x, 
# return the index i. If the entire array is traversed without finding x, return -1.
# Time: O(n)
# Space: O(1)

# 2) Optimal Approach - Use binary search and identify which half is sorted. 
# If the left half is sorted and x lies within its range, search the 
# left half; otherwise search the right half. If the right half is sorted, 
# check whether x lies within its range and choose the appropriate half. 
# This discards half of the search space at each step.
# Time: O(log n)
# Space: O(1)


# 1) Brute Force Approach -
'''
nums = [4, 5, 6, 7, 0, 1, 2]
x = 0
index = -1

for i in range(len(nums)):
    if nums[i] == x:
        index = i
        break

if index == -1:
    print("Element is not present")
else:
    print("The element is present at index:", index)'''
    
        
# 2) Optimal Approach -
nums = [4, 5, 6, 7, 0, 1, 2]
x = 0
index = -1
low = 0
high = len(nums) - 1

while(low <= high):
    mid = (low + high) // 2

    if nums[mid] == x:
        index = mid
        break

    # Left half is sorted and target lies there
    elif nums[low] <= nums[mid] and (x >= nums[low] and x < nums[mid]):
        high = mid - 1

    # Right half is sorted and target lies there
    elif nums[mid] <= nums[high] and (x > nums[mid] and x <= nums[high]):
        low = mid + 1

    # Target is not in the sorted half
    else:
        if nums[low] <= nums[mid]:
            low = mid + 1
        else:
            high = mid - 1

if index == -1:
    print("Element is not present")
else:
    print("The element is present at index:", index)