# Highest Occurring Element in an Array.

# Problem statement - Given an array of size N. Find the highest and lowest frequency element.

# Author - Rajiv Das
# Date - 20-08-2026
# ----------------------------------------------------------

# Two approaches for doing this - 

# 1) Brute Force Approach - will use 2 loops that will take O(n^2) time and O(1) space complexity.

# 2) Optimal Approach - gonna use Hashing will take O(n) time and o(n) space complexity.


# 1) Brute Force Approach -
'''
arr = [10, 5, 7, 9, 10]
maxelement = arr[0]
maxcount = 0

for i in range(len(arr)):
    count = 0
    for j in range(len(arr)):
        if arr[j] == arr[i]:
            count += 1

    if count > maxcount:
        maxcount = count
        maxelement = arr[i]

print(f"The element with highest count is- {maxelement} : {maxcount}")
'''

# 2) Optimal Approach -
'''
arr = [10, 5, 7, 9, 10, 9, 9]
count = 0
freq = {}

for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)

for key, value in freq.items():
    if value > count:
        count = value
        element = key

print(f"The element with highest count is- {element} : {count}")'''


# STRIVER'S ACTUAL QUESTION - Given an array nums of n integers, find the most frequent 
# element in it i.e., the element that occurs the maximum number of times. If there are 
# multiple elements that appear a maximum number of times, find the smallest of them.
# Example 1 - Input: nums = [1, 2, 2, 3, 3, 3]
#             Output: 3
#             Explanation: The number 3 appears the most (3 times). It is the most frequent element.
# Example 2 - Input: nums = [4, 4, 5, 5, 6]
#             Output: 4
#             Explanation: Both 4 and 5 appear twice, but 4 is smaller. So, 4 is the most frequent element.

arr = [10, 5, 1, 9, 20, 10, 5, 4, 5, 10]
#arr = [1, 1, 2, 2, 2, 10]
count = 0
freq = {}

for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)

element = float('inf')
for key, value in freq.items():
    if value > count:
        count = value
        element = key
    elif value == count and key < element:
        element = key

print(f"The element with highest count is- {element} : {count}")