# Print Subarray with Maximum Sum (Extended Kadane’s Algorithm).

# Problem Statement - Given an integer array nums, find the contiguous subarray 
# that has the maximum possible sum. Return/print both the maximum sum and the 
# elements of the subarray that produce this sum.

# Author - Rajiv Das
# Date - 19-08-2026
# ----------------------------------------------------------

# Two approaches for doing this - 

# 1) Brute Force Approach - Use two nested loops to generate all possible 
# contiguous subarrays. The outer loop i selects the starting index and resets 
# total = 0, while the inner loop j extends the subarray from i to the end. 
# Add nums[j] to total for each element. If total > maxtotal, update maxtotal, 
# start = i, and end = j. Finally, nums[start:end + 1] gives the maximum subarray. 
# float("-inf") ensures the program also works when all elements are negative.
# Time Complexity: O(n^2).
# Space Complexity: O(1).


# 2) Optimal Approach - Kadane's Algorithm
# Loop through the array and add nums[i] to currenttotal. If nums[i] > currenttotal, 
# discard the previous negative contribution and start a new subarray from i using 
# tempstart. If currenttotal > maxtotal, update maxtotal, start = tempstart, and 
# end = i. float("-inf") ensures the program also works when all elements are negative.
# Time Complexity: O(n).
# Space Complexity: O(1).


# 1) Brute Force Approach -
'''
nums = [-2, -3, -7, -2, -10, -4]  
maxtotal = float("-inf")
start = 0
end = 0

for i in range(len(nums)):
    total = 0
    for j in range(i, len(nums)):
        total = total + nums[j]

        if total > maxtotal:
            maxtotal = total
            start = i
            end = j

print("Maximum subarray sum:", maxtotal)
print("Subarray:", nums[start:end + 1])'''


# 2) Optimal Approach - Kadane's Algorithm
nums = [2,-3,-4,3,1,4,2,-4,-5]  
currenttotal = 0
maxtotal = float("-inf")

start = 0
end = 0
tempstart = 0

for i in range(len(nums)):

    currenttotal += nums[i]

    if nums[i] > currenttotal:
        tempstart = i
        currenttotal = nums[i]

    if currenttotal > maxtotal:
        start = tempstart
        end = i
        maxtotal = currenttotal

print("Maximum subarray sum:", maxtotal)
print("Subarray:", nums[start:end + 1])