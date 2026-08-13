# Remove Duplicates in-place from Sorted Array

# Problem Statement - Given an integer array sorted in non-decreasing order, 
# remove the duplicates in place such that each unique element appears 
# only once. The relative order of the elements should be kept the same. 
# If there are k elements after removing the duplicates, then the 
# first k elements of the array should hold the final result. It doesn't matter 
# what you leave beyond the first k elements.

# Author - Rajiv Das
# Date - 13-08-2026
# ----------------------------------------------------------

# There are 2 approaches :-

# 1) Brute force approach - Since we need to store only unique elements, we can use the 
# set data structure. We can insert all the elements of the array in the set irrespective 
# of their frequency as set only allows one occurence of each element.Declare a set and 
# insert all the elements of the array into the set.The number of unique elements in array 
# is equal to size of the set.Traverse the set and fill the first k indices 
# with elements in set.

# 2) Optimal Approach - Instead of using a set to store the unique elements, we can 
# implement a two pointer strategy to optimize the space. Since the array is sorted, we 
# know that all the duplicate values will be adjacent to each other.


# 1) Brute force approach - Time complexity - O(n)
                          # Space complexity - O(n)
'''
arr = [2,2,3,4,4,5,6,6,6]
a = set()
index = 0

for i in arr:
    if i not in a:
        a.add(i)
        arr[index] = i #It also updates the original array.
        index += 1

print(a)
print(arr)
print(index)'''


# 2) Optimal Approach - Time complexity - O(n)
                      # Space complexity - O(1)

arr = [2,2,3,4,4,5,6,6,6]
index = 0

for i in range(1, len(arr)):
    if arr[index] != arr[i]:
        index += 1
        arr[index] = arr[i]

print(arr) # You have to ignore the remaining elements after the unique ones.