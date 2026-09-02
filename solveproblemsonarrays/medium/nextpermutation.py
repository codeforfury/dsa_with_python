# Next Permutation.

# Problem Statement - Given an array of integers nums, rearrange the elements 
# of the array into the lexicographically next greater permutation. 
# If no such permutation exists, rearrange the array into the lowest 
# possible order, i.e., sort the array in ascending order. 
# The rearrangement must be performed in-place using only constant extra space.

# Author - Rajiv Das
# Date - 02-09-2026
# ----------------------------------------------------------

# There are Two approaches for doing this but we will do only 
# the optimal one as this is only necessary- 


# 1) Optimal Approach - # 2) Optimal Approach - Find the pivot by traversing from right to left.
# If no pivot is found, the array is already in descending order,
# so reverse the entire array to get the lowest possible permutation.
# Otherwise, find the smallest element greater than the pivot from the right,
# swap them, and reverse the elements after the pivot.
# Time Complexity: O(n).
# Space Complexity: O(1).


# 1) Optimal Approach - 
nums = [1, 2, 5, 4, 3]

# Initially assume that no pivot exists
pivot = -1

# Traverse the array from right to left
# Find the first position where nums[i] < nums[i+1]
for i in range(len(nums) - 2, -1, -1):
    if nums[i] < nums[i + 1]:
        pivot = i
        break

# If no pivot is found, the array is already in descending order.
# Therefore, it is the largest possible permutation.
# Reverse the entire array to get the smallest permutation.
if pivot == -1:
    print("The array is already in descending order, so the lowest possible permutation is:")
    nums.reverse()
    print(nums)

else:
    # Traverse from the right side and find the first element
    # greater than the pivot.
    for i in range(len(nums) - 1, pivot, -1):
        if nums[i] > nums[pivot]:

            # Swap the pivot with the next greater element
            nums[i], nums[pivot] = nums[pivot], nums[i]
            break

    # Reverse the elements after the pivot.
    # This makes the remaining part as small as possible.
    left = pivot + 1
    right = len(nums) - 1

    while left < right:

        # Swap elements from both ends
        nums[left], nums[right] = nums[right], nums[left]

        # Move the pointers towards the center
        left += 1
        right -= 1

    # Print the final next permutation
    print("The next permutation is:", nums)