# Reverse a given Array.

# Problem Statement: You are given an array. The task is to reverse the array and print it.

# Author - Rajiv Das
# Date - 22-08-2026
# ----------------------------------------------------------

# There are 3 approaches for this -

# 1)Brute Force Approach - A straightforward way is to create a new array and start 
# placing the original array's elements from the back into the front of the new array.
# Time complexity: O(n)
# Space complexity: O(n)

# 2)Better Approach - It uses two pointers to simultaneously traverse the array from both ends, 
# swapping the elements until the center is reached. This way, we avoid creating a new 
# array and perform the reverse operation efficiently using constant space.
# Time complexity: O(n)
# Space complexity: O(1), Does In-place reverse.

# 3)Built-in Library Function Approach - In Python, array slicing with a step of -1 
# creates a reversed copy of the array. It doesn’t reverse in-place unless you 
# explicitly overwrite the original array with the result.


# 1)Brute Force approach -
'''
arr = [5,4,7,2,1,8,9]
copy = []

for i in arr[-1::-1]:
    copy.append(i)

print(copy)
'''

# 2)Better approach -
'''
arr = [3,7,1,3,12,5,10]
i = 0
j = len(arr) - 1

while i < j:
    arr[i],arr[j] = arr[j],arr[i]
    i += 1
    j -=1

print(arr)
'''

# 3)Built-in Library Function Approach -

arr = [8,7,1,3,4,10,9]
arr.reverse() # Does in-place reversal, internally uses 2 pointer concept only.
print(arr)