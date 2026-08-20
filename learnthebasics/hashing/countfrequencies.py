# Count frequency of each element in the array.

# Problem steatement - Given an array, we find the number 
# of occurrences of each element in the array.

# Author - Rajiv Das
# Date - 20-08-2026
# ----------------------------------------------------------

# Two approaches for doing this - 

# 1) brute Force Approach - We use a visited array of boolean values to keep track of 
# which elements have already been counted. For each element in the array, if it has not 
# been visited, we iterate over the rest of the array to count how many times it appears. 
# After counting, we mark the duplicates as visited to avoid recounting them.
# Time Complexity: O(N²), as for every element we may scan the remaining elements in the array.
# Space Complexity: O(N), for the visited array of size N.

# 2) Optimal Approach - We want to count how many times each element appears in the array. 
# Using a hash map allows us to track frequencies efficiently as we traverse the array, 
# avoiding the need for nested loops.
# Time Complexity: O(N), where N is the number of elements in the array. Each element is processed once.
# Space Complexity: O(N), for storing frequencies of unique elements in the unordered_map.


# 1) Brute Force Approach -
'''
arr = [10, 5, 10, 15, 10, 5]
visited = []
count = 0

for i in range(len(arr)):
    if arr[i] in visited: #this (in) searches for the element in visited list. so extra O(k) complexity is happening.
        continue          # But this version of program is easier to understand than the brute force 
    else:                 # approach mention ealier i.e maintaining a boolean array.
        visited.append(arr[i])
        count = 1
        for j in range(i+1, len(arr)):
            if arr[j] == arr[i]:
                count += 1
        print(arr[i],count)
        count = 0
'''

# 2) Optimal Approach - Using Hash Approach (in python we can use Dictionary)
arr = [0,0]
freq = {}

for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)