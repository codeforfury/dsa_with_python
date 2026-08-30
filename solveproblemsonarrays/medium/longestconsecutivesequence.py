# Longest Consecutive Sequence in an Array.

# Problem Statement - Given an unsorted array of integers, find the 
# length of the longest sequence of consecutive integers present 
# in the array. The consecutive numbers can appear in any order 
# in the original array.

# Author - Rajiv Das
# Date - 30-08-2026
# ----------------------------------------------------------

# Two approaches for doing this - 

# 1) Brute Force Approach - For each element, consider it as the starting element of a consecutive sequence.
# Start count = 1.
# Set the next number to search as current + 1.
# Use while current in nums to check whether the next consecutive number exists.
# If it exists, increase count and search for the next number.
# Continue until the next consecutive number is not found.
# Update maxcount with the maximum sequence length found. 
# Time Complexity: O(n²) — in the worst case, because in on a list takes O(n), and the nested searching can happen for multiple starting elements.
# Space Complexity: O(1)


# 2) Better Approach - Sort the array first so that consecutive elements come next to each other.
# Use nums.sort() to sort the array.
# Traverse the sorted array from left to right.
# If the next element is exactly 1 greater than the current element, increase count.
# If the next element is a duplicate, ignore it using continue.
# If the next element is neither consecutive nor a duplicate, reset count to 1.
# Keep track of the maximum count using maxcount.
# Time Complexity: O(n log n) — sorting takes O(n log n) and traversal takes O(n).
# Space Complexity: O(1).


# 3) Optimal Approach - Use a Hash Set to store all elements of the array, 
# which automatically removes duplicates and provides O(1) average-time lookup. 
# Traverse each element i in the set and check whether i - 1 exists; 
# if it exists, skip i because it is not the start of a sequence. 
# If i - 1 does not exist, i is the starting point, 
# so check i + 1, i + 2, i + 3, etc. using the set and keep increasing 
# the count while each consecutive number exists. Finally, keep 
# track of the maximum sequence length. The important trick is to start 
# counting only from the first element of each sequence, which prevents 
# repeatedly scanning the same sequence and gives an average 
# time complexity of O(n). The space complexity is O(n) for the Hash Set. 
# Time Complexity: O(n) on Average.
# Space Complexity: O(n) for Hash Set.


# 1) Brute Force Approach -
'''
nums = [100, 3, 4, 200, 1, 3, 2]
maxcount = 0
a = 1

for i in nums:
    count = 1
    a = i + 1 
    while a in nums:
        count += 1
        a += 1
    
    maxcount = max(maxcount, count)

print("Count of max consecutive sequence is:", maxcount)'''


# 2) Better Approach -
'''
nums = [1, 2, 3, 3, 4, 100, 200, 201, 202, 203, 204, 205]
maxcount = 1
count = 1
nums.sort()
# [1, 2, 3, 3, 4, 100, 200, 201, 202, 203, 204]

for i in range(len(nums)-1):
    if nums[i+1] == nums[i] + 1:
        count += 1
        maxcount = max(maxcount, count)

    elif nums[i+1] == nums[i]:
        continue

    else:
        count = 1

print("Count of max consecutive sequence is:", maxcount)'''


# 3) Optimal Approach -
nums = [1, 2, 3, 3, 4, 100, 200, 201, 202, 202, 203, 204, 205]
s = set(nums)
maxcount = 1

for i in s:

    # If the previous number exists, i is not the start of a sequence
    if (i-1) in s:
        continue

    # Start counting the consecutive sequence from i
    count = 1
    a = i + 1
    # Keep checking for the next consecutive number
    while a in s:
        count += 1
        a += 1

    # Keep the length of the longest sequence found so far
    maxcount = max(maxcount, count)

print("Count of max consecutive sequence is:", maxcount)