# Minimum in Rotated Sorted Array.

# Problem Statement - Given an integer array arr of size N, sorted in 
# ascending order (with distinct values), the array is rotated 
# at any index which is unknown. Find the minimum element in the array.

# Author - Rajiv Das
# Date - -08-2026
# ----------------------------------------------------------

# Two approaches for doing this - 

# 1) Brute Force Approach - Traverse the array and keep track of the 
# smallest element found so far. Compare each element 
# with minimum and update it whenever a smaller value is found.
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
nums = [4,5,6,7,0,1,2,3]
minimum = nums[0]

for i in range(len(nums)):
    if nums[i] <= minimum:
        minimum = nums[i]

print("Minimum is:", minimum)'''
    
        
# 2) Optimal Approach -
nums = [4, 5, 6, 7, 0, 1, 2]
low = 0
high = len(nums) - 1

while(low < high):
    mid = (low + high) // 2

    # If nums[mid] is greater than nums[high],
    # the minimum lies in the right half
    if nums[mid] > nums[high]:
        low = mid + 1

    # Otherwise, the minimum lies at mid or in the left half
    else:
        high = mid

# When low == high, we have reached the minimum element
print("Minimum is:", nums[low])