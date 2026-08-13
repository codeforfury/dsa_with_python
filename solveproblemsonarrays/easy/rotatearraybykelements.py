# Rotate array by K elements.

# Problem Statement - Given an array of integers, rotating array of elements 
# by k elements either left or right.

# Author - Rajiv Das
# Date - 13-08-2026
# ----------------------------------------------------------

# There are 2 approaches :-

# 1) Brute force approach - 
# Right Rotation: We store the last k elements of the array into a 
# temporary array. Then we shift all the other elements (n-k elements) to the right by k positions. 
# Finally, we place the elements from the temporary array at the beginning of the original array. 
# This achieves a right rotation by k positions.
# Take the last k elements and store them in a temporary array.
# Shift the first n-k elements to the right by k positions.
# Copy the k stored elements from the temporary array to the start of the original array.

# Left Rotation: We store the first k elements in a temporary array. Then we shift the remaining n-k 
# elements to the left by k positions. Finally, we copy the elements from the temporary array to the 
# end of the array. This achieves a left rotation by k positions.
# Store the first k elements in a temporary array.
# Shift the remaining elements to the left by k positions.
# Copy the k stored elements to the end of the original array.

# 2) Optimal Approach - Instead of simulating each rotation one by one, we can get the rotated array in-place by reversing specific 
# parts of the array. This works because rotating is just rearranging sections of the array.
# For Left Rotation by k steps:
# Reverse the first k elements
# Reverse the remaining n - k elements
# Reverse the entire array

# For Right Rotation by k steps:
# Reverse the entire array
# Reverse the first k elements
# Reverse the remaining n - k elements

# 1) Brute force approach - (left rotate by k places) Time Complexity: O(n) Space Complexity: O(k)
''' 
nums = [1, 2, 3, 4, 5, 6, 7]
k = 2
temp = nums[:k]
k = k % len(nums)
for i in range(k, len(nums)):
    nums[i - k] = nums[i]

for i in range(k):
    nums[len(nums) - k + i] = temp[i]

print(nums)'''

# (Now right rotate by k places)
'''
nums = [1, 2, 3, 4, 5, 6, 7]
k = 2
k = k % len(nums)
temp = nums[-k:]

for i in range(len(nums) - k - 1, -1, -1):
    nums[i + k] = nums[i]

for i in range(k):
    nums[i] = temp[i]

print(nums)'''



# 2) Optimal Approach - (left rotate by k places) Time Complexity: O(n) Space Complexity: O(1)
'''
nums = [1, 2, 3, 4, 5, 6, 7]
k = 2
k = k % len(nums)

def reverse(nums, start, end):
    while(start < end):
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

reverse(nums, 0, k - 1)             # REVERSE FIRST K ELEMENTS
reverse(nums, k, len(nums) - 1)     # REVERSE THE REMAINING N-K ELEMENTS
reverse(nums, 0, len(nums) - 1)     # REVERSE THE ENTIRE ARRAY

print(nums)'''


# (Now right rotate by k places)
nums = [1, 2, 3, 4, 5, 6, 7]
k = 2
k = k % len(nums)

def reverse(nums, start, end):
    while(start < end):
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

reverse(nums, 0, len(nums) - 1)     # REVERSE THE ENTIRE ARRAY
reverse(nums, 0, k - 1)             # REVERSE FIRST K ELEMENTS
reverse(nums, k, len(nums) - 1)     # REVERSE THE REMAINING N-K ELEMENTS

print(nums)