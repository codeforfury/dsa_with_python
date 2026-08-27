# Search Element in Rotated Sorted Array II.

# Problem Statement - Given an integer array arr of size N, sorted in 
# ascending order (may contain duplicate values) and a target value k. 
# Now the array is rotated at some pivot point unknown to you. 
# Return True if k is present and otherwise, return False.

# Author - Rajiv Das
# Date - 27-08-2026
# -----------------------------------------------------------

# Two approaches for doing this - 

# 1) Brute Force Approach - Traverse the array from left to right and 
# compare each element with x. If nums[i] == x, return True; 
# otherwise, after checking the entire array, return False.
# Time: O(n)
# Space: O(1)

# 2) Optimal Approach - Use modified binary search. 
# If nums[low] == nums[mid] == nums[high], shrink the search range 
# using low += 1 and high -= 1. Otherwise, identify the sorted half 
# and check whether x lies in that range; then search the appropriate half.
# Time: Average: O(log n), Worst case: O(n) because duplicates may force us to shrink one element from each side repeatedly.
# Space: O(1)


# 1) Brute Force Approach -
'''
nums = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
x = 4

for i in range(len(nums)):
    if nums[i] == x:
        print(True)
        break

else:
    print(False)'''
    
        
# 2) Optimal Approach -

nums = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
x = 3
low = 0
high = len(nums) - 1

while(low <= high):
    mid = (low + high) // 2

    # If middle element is the target, target is found
    if nums[mid] == x:
        print(True)
        break

    # If low, mid and high are equal, we cannot identify the sorted half
    # So, shrink from both ends.
    elif nums[low] == nums[mid] == nums[high]:
        low += 1
        high -= 1

    # Left half is sorted and target lies within the left half
    elif nums[low] <= nums[mid] and (x >= nums[low] and x < nums[mid]):
        high = mid - 1

    # Right half is sorted and target lies within the right half
    elif nums[mid] <= nums[high] and (x > nums[mid] and x <= nums[high]):
        low = mid + 1

    # Target is not in the identified sorted half
    else:
        # If left half is sorted, search in the right half
        if nums[low] <= nums[mid]:
            low = mid + 1

        # Otherwise, right half is sorted, so search in the left half
        else:
            high = mid - 1

# If the loop completes without finding the target
else:
    print(False)