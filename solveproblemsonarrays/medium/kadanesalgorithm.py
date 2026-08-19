# Kadane's Algorithm : Maximum Subarray Sum in an Array.

# Problem Statement - Given an integer array nums, find the subarray with the largest 
# sum and return the sum of the elements present in that subarray. 
# A subarray is a contiguous non-empty sequence of elements within an array.

# Author - Rajiv Das
# Date - 19-08-2026
# ----------------------------------------------------------

# Two approaches for doing this - 

# 1) Brute Force Approach - Use two nested loops to generate all possible contiguous 
# subarrays. The outer loop selects the starting index of the subarray. The inner 
# loop extends the subarray from that starting index. Keep adding elements to total 
# to calculate the sum of the current subarray. Update maxtotal whenever a larger sum 
# is found. Initialize maxtotal with float("-inf") so that the algorithm also works 
# when all elements are negative.
# Time Complexity: O(n^2).
# Space Complexity: O(1).


# 2) Optimal Approach - Kadane's Algorithm
# Kadane's Algorithm finds the maximum sum of a contiguous subarray in O(N) time.
# Maintain two variables:
# currenttotal → maximum sum of the subarray ending at the current element.
# maxtotal → maximum sum found so far.
# For each element, decide whether to:
# Start a new subarray with the current element, or
# Continue the existing subarray by adding the current element.
# Time Complexity: O(n).
# Space Complexity: O(1).


# 1) Brute Force Approach -
'''
nums = [2, 3, 5, -2, 7, -4]
maxtotal = float("-inf")

for i in range(len(nums)):
    total = 0
    for j in range(i, len(nums)):
        total = total + nums[j]
        maxtotal = max(maxtotal, total)

print(maxtotal)'''


# 2) Optimal Approach - Kadane's Algorithm
nums = [2, 3, 5, -2, 7, -4]
currenttotal = 0
maxtotal = float("-inf")

for i in nums:

    currenttotal = max(i, currenttotal + i)
    maxtotal = max(maxtotal, currenttotal)

print(maxtotal)