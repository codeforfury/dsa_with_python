# Sort an array of 0s, 1s and 2s

# Problem Statement - Given an array nums consisting of only 0, 1, or 2. 
# Sort the array in non-decreasing order. The sorting must be done in-place, 
# without making a copy of the original array.

# Author - Rajiv Das
# Date - 18-08-2026
# ----------------------------------------------------------

# Three  approaches for doing this - 

# 1) Brute Force Approach - Just sort the array and print it.(We Know this)
# Time Complexity: O(n log n)
# Space Complexity: O(1)

# 2) Better Approach - We are given an array containing only 0s, 1s, and 2s. 
# Since the values are fixed and known, the simplest approach is to first count 
# how many 0s, 1s, and 2s are present in the array. After counting, we overwrite 
# the original array based on the frequency of these values first fill it with 0s, 
# then 1s, then 2s. This does not require any extra array and 
# modifies the input array in-place.
# Time Complexity: O(n),We traverse the array twice: once to count, once to overwrite. Each operation is O(n).
# Space Complexity: O(1), We use only a constant number of counters 

# 3) Optimal Approach - Dutch National Flag Algorithm
# Uses three pointers: low, mid, and high to divide the array into regions of 0s, 1s, unknown elements, and 2s.
# If nums[mid] == 0, swap with low and move both pointers.
# If nums[mid] == 1, move mid.
# If nums[mid] == 2, swap with high and move only high.
# This sorts the array in one pass without using extra space.
# Time Complexity: O(n).
# Space Complexity: O(1).


# 2) Better Approach - 
'''
arr = [2,0,1,0,1,1,2,2,1]
c0 = c1 = c2 = 0

for i in arr:
    if i == 0:
        c0 += 1
    elif i == 1:
        c1 += 1
    else:
        c2 += 1

index = 0
for i in range(c0):
    arr[index] = 0
    index += 1

for i in range(c1):
    arr[index] = 1
    index += 1

for i in range(c2):
    arr[index] = 2
    index += 1

print(arr)'''


# 3) Optimal Approach - Dutch National Flag Algorithm.
arr = [2,0,1,0,1,1,2,2,1,0,2]
low = 0
mid = 0
high = (len(arr) - 1)

while (mid <= high):
    if arr[mid] == 0:
        arr[low], arr[mid] = arr[mid], arr[low]
        low += 1
        mid += 1

    elif arr[mid] == 1:
        mid += 1

    else:
        arr[mid], arr[high] = arr[high], arr[mid]
        high -= 1

print(arr)