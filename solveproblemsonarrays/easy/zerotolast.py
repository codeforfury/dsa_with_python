# Move all Zeros to the end of the array

# Problem Statement - You are given an array of integers, your task is 
# to move all the zeros in the array to the end of the array and move 
# non-negative integers to the front by maintaining their order.

# Author - Rajiv Das
# Date - 14-08-2026
# ----------------------------------------------------------

# There are 2 approaches :-

# 1) Brute force approach - we can think of, involves the use of an extra array. Firstly intialise it with all zero
# then copy the non zeros element at the starting of the temp array.

# 2) Optimal Approach - Create a variable called max and initialize it with the value of 
# the first element in the array. Use a for loop to iterate through the rest of 
# the elements in the array.


# 1) Brute force approach - Time and Spae comp: O(n).
'''
arr = [4,0,0,2,8,0,7,0]
temp = [0] * len(arr)
index = 0

for i in arr:
    if i != 0:
        temp[index] = i
        index += 1

print(temp)'''


# 2) Optimal Approach -
arr = [4,0,6,2,8,0,7,0]
pointer = 0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[pointer], arr[i] = arr[i], arr[pointer]
        pointer += 1

print(arr)