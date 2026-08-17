# Longest Subarray with given Sum K(Positives).

# Problem Statement - Given an array nums of size n and an integer k, find the 
# length of the longest sub-array that sums to k. If no such sub-array exists, return 0.

# Author - Rajiv Das
# Date - 16-08-2026
# ----------------------------------------------------------

# There are 2 approaches :-

# 1) Brute force approach - Using for loop inside a for loop.

# 2) Optimal Approach - Using Two pointer sliding window.


# 1) Brute force approach - Time: O(n^2) and Space: O(1) complexity.
'''
nums = [10, 5, 20, 7, 1, 9]
k = 15  
c = 0
maxcount = 0
sum = 0
for i in range(len(nums)):
    for j in range(i, len(nums)):
        sum += nums[j]
        c += 1
        if sum == k:
            maxcount = max(maxcount, c)
    c = 0
    sum = 0
print(maxcount)'''



# 2) Optimal Approach - Time: O(n) and Space: O(1) complexity.
nums = [10, 5, 2, 7, 1, 9]
k = 15
c = 0
maxcount = 0
total = 0
i = j = 0
while(j < len(nums)):
    total += nums[j]
    c += 1

    while total > k:
        total -= nums[i]
        c -= 1
        i += 1

    if total == k:
        maxcount = max(maxcount, c)

    j += 1

print(maxcount)