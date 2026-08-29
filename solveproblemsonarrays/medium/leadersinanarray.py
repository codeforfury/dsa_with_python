# Leaders in an Array.

# Problem Statement - Given an array of integers, find all the leader elements 
# in the array. An element is called a leader if it is greater than all 
# the elements to its right. The rightmost element is always a leader 
# because there are no elements to its right. Return all the leader elements.

# Author - Rajiv Das
# Date - 29-08-2026
# ----------------------------------------------------------

# Two approaches for doing this - 

# 1) Brute Force Approach - For every element, check all the elements to its right.
# If the current element is greater than every element on its right, it is a leader.
# The rightmost element is always a leader because there is nothing to its right.
# Store all the leader elements in a result list.
# Time Complexity: O(n²) — for each element, we may check all elements to its right.
# Space Complexity: O(n) for storing the output leaders.


# 2) Optimal Approach - Traverse the array from right to left while keeping 
# track of the maximum element seen so far. The rightmost element is 
# always a leader. If the current element is greater than maximum, 
# it is a leader. Add it to the result and update maximum. Since 
# leaders are collected from right to left, reverse the result at the end.
# Time Complexity: O(n).
# Space Complexity: O(n) — for storing the leaders.


# 1) Brute Force Approach -
'''
nums = [10, 22, 12, 3, 0, 6]
result = []

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] <= nums [j]:
            break
    else:
        result.append(nums[i])

print(result)'''

# 2) Optimal Approach - 
nums = [10, 22, 12, 3, 0, 6]
result = []

# The rightmost element is always a leader
result.append(nums[-1])
maximum = nums[-1]

# Traverse the array from right to left
for i in range(len(nums) - 2, -1, -1):

    # Current element is a leader if it is greater than
    # every element to its right
    if nums[i] > maximum:
        result.append(nums[i])
        maximum = nums[i]

# Leaders were collected from right to left,
# so reverse them to get their original order
result.reverse()

print(result)