# Find the Majority Element that occurs more than N/2 times.

# Problem Statement - Given an integer array nums of size n, return the 
# majority element of the array. The majority element of an array is an 
# element that appears more than n/2 times in the array. The array is 
# guaranteed to have a majority element.

# Author - Rajiv Das
# Date - 19-08-2026
# ----------------------------------------------------------

# Three approaches for doing this - 

# 1) Brute Force Approach - Iterate through the array to select each element 
# one by one. For each selected element, run another loop to count its 
# occurrences in the given array. If the occurrence of any element is greater 
# than the floor of (N/2), return that element immediately as the majority element.
# Time Complexity: O(n^2).
# Space Complexity: O(1).

# 2) Better Approach - Hash Map:
# Use a dictionary to store the frequency of each element.
# Traverse the array and increase the element's count whenever it appears.
# After each count update, immediately check if the count is greater than N/2.
# If it is, return/print that element immediately.
# Time Complexity: O(n).
# Space Complexity: O(n) for Hash Map.

# 3) Optimal Approach - Boyer-Moore Voting Algorithm
# Maintain two variables: candidate and count.
# If count == 0, choose the current element as the new candidate.
# If the current element equals the candidate, increase count.
# Otherwise, decrease count because the two different elements effectively cancel each other.
# After traversing the array, the candidate is the majority element if a majority element is guaranteed to exist.
# If a majority element is not guaranteed, perform a second pass to verify that the candidate occurs more than N/2 times.
# Time Complexity: O(n).
# Space Complexity: O(1).


# 1) Brute Force Approach -
''' 
arr = [7, 0, 0, 1, 7, 7, 2, 7, 7]
c = 0
found = False

for i in range(len(arr)):
    c = 0
    for j in range(len(arr)):
        if arr[j] == arr[i]:
            c += 1
            if c > (len(arr)/2):
                print("The Majority element is:", arr[i])
                found = True
                break
    if found:
        break'''


# 2) Better Approach - Using Hash Map
'''
arr = [7, 0, 0, 1, 7, 7, 2, 7, 7]
freq = {}

for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

    if freq[i] > len(arr) / 2:
        print("The Majority element is:", i)
        break'''


# 3) Optimal Approach - Boyer-Moore Voting Algorithm
arr = [7, 0, 0, 1, 7, 7, 2, 7, 7]
candidate = 0
count = 0

# First pass: Find the potential majority element
# ***THIS SINGLE PASS IS ONLY ENOUGH IF THE MAJORITY ELEMENT IS GUARANTEED***
for i in arr:

    # If count becomes 0, choose the current element as candidate
    if count == 0:
        candidate = i

    # Same element supports the candidate
    if i == candidate:
        count += 1

    # Different element cancels the candidate
    else:
        count -= 1

# Second pass: Verify whether the candidate is actually a majority
count = arr.count(candidate)

# Majority element must occur more than N/2 times. If a majority element is not guaranteed, perform 
# a second pass to verify that the candidate occurs more than N/2 times.
if count > len(arr) // 2:
    print("The Majority element is:", candidate)
else:
    print("There is no majority element")