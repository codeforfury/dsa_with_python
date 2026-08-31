# Search element X in sorted array.

# Problem Statement - You are given a sorted array of integers and a target, your 
# task is to search for the target in the given array. Assume the 
# given array does not contain any duplicate numbers.

# Author - Rajiv Das
# Date - 24-08-2026
# ----------------------------------------------------------

# Two approaches for doing this - 

# 1) Iterative Implementation - Set low = 0 and high = len(nums) - 1. 
# Calculate mid = (low + high) // 2. If nums[mid] == target, the element is found. 
# If target > nums[mid], search the right half by setting low = mid + 1; otherwise, 
# search the left half by setting high = mid - 1. Continue while low <= high. If the 
# loop ends, the element is not found.
# Time: O(log n) — the search space is halved each iteration.
# Space: O(1) — iterative implementation uses constant extra space.

# 2) Recursive Approach - Calculate mid = (low + high) // 2. If nums[mid] == target, 
# the element is found. If target > nums[mid], recursively search the right half using 
# binarysearch(mid + 1, high); otherwise, recursively search the left half using 
# binarysearch(low, mid - 1). If low > high, stop the recursion and report that the 
# element is not found.
# Time: O(log n) — the search space is halved at each recursive call.
# Space: O(log n) — recursive calls use the call stack.


# 1) Iterative Implementation -
'''
nums = [3, 4, 6, 7, 9, 12, 16, 17]
low = 0
high = len(nums) - 1
target = 17

while(low <= high):
    mid = (low + high) // 2

    if nums[mid] == target:
        print("Element found at index:", mid)
        break

    elif target > nums[mid]:
        low = mid + 1

    else:
        high = mid - 1

else:
    print("Element not found")'''


# 2) Recursive Approach -
nums = [3, 4, 5, 6, 7, 9, 12, 16, 17, 20]
low = 0
high = len(nums) - 1
target = 1

def binarysearch(low, high):
    if low > high:
        print("Element not found")
        return
    
    mid = (low + high) // 2

    if nums[mid] == target:
        print("Element found at index:", mid)
    
    elif target > nums[mid]:
        binarysearch(mid + 1, high)
    
    else:
        binarysearch(low, mid - 1)

binarysearch(low, high)