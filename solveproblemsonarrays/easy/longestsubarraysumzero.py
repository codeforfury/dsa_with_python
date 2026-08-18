# Length of the longest subarray with zero Sum

# Problem Statement - Given an array containing both positive and 
# negative integers, we have to find the length of the longest subarray 
# with the sum of all elements equal to zero.

# Author - Rajiv Das
# Date - 18-08-2026
# ----------------------------------------------------------

# There are 2 approaches :-

# 1) Brute force approach - Using for loop inside a for loop.

# 2) Optimal Approach - Using Prefix sum and Hash map concept.


# 1) Brute force approach - Time: O(n^2) and Space: O(1) complexity.
'''
nums = [6, -2, 2, -8, 1, 7, 4, -10]
c = 0
maxcount = 0
sum = 0
for i in range(len(nums)):
    for j in range(i, len(nums)):
        sum += nums[j]
        c += 1
        if sum == 0:
            maxcount = max(maxcount, c)
    c = 0
    sum = 0
print(maxcount)'''


# ** THIS PROGRAM IS CRITICAL **
# 2) Optimal Approach - Time: O(n) and Space: O(n) complexity.
arr = [6, -2, 2, -8, 1, 7, 4, -10]
freq = {}
prefix_sum = 0
max_length = 0

for i in range(len(arr)):
    prefix_sum += arr[i]

    if prefix_sum == 0:
        max_length = i - 0 + 1   # last index - first index + 1

    elif prefix_sum in freq:
        length = i - freq[prefix_sum]
        max_length = max(max_length, length)

    else:
        freq[prefix_sum] = i

print(max_length)