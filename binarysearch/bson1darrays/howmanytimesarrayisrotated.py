# Find out how many times the array has been rotated.

# Problem Statement - Given an integer array arr of size N, sorted in 
# ascending order (with distinct values). Now the array is rotated 
# between 1 to N times which is unknown. Find how many times 
# the array has been rotated.

# Author - Rajiv Das
# Date - 28-08-2026
# ----------------------------------------------------------

# Two approaches for doing this - 

# 1) Brute Force Approach - Traverse the array to find the minimum element. 
# The index of the minimum element is equal to the 
# number of times the array has been rotated.
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
    if nums[i] < minimum: # We use < here, cuz we have distinct values.
        minimum = nums[i]
        index = i

print("The no. of times the array is rotated:", index)'''
    
        
# 2) Optimal Approach -
nums = [4, 5, 6, 7, 8, 9, 10, 0, 1, 2]
low = 0
high = len(nums) - 1

while(low < high):
    mid = (low + high) // 2

    # If nums[mid] is greater than nums[high],
    # the minimum lies in the right half.
    if nums[mid] > nums[high]:
        low = mid + 1

    # Otherwise, the minimum lies at mid or in the left half.
    else:
        high = mid

# When low == high, we have reached the minimum element.
# The index of the minimum element is the number of rotations.
print("The no. of times the array is rotated:", low)