# Find the largest element in an array.
# Problem Statement - Given an array, we have to find the largest element in the array.
# Author - Rajiv Das
# Date - 12-08-2026
# ----------------------------------------------------------

# There are 2 approaches :-

# 1) Brute force approach - Sort the array in ascending order. Print the element at 
# the (size of the array - 1)th index, which corresponds to the largest element in 
# the array. We already know this!

# 2) Optimal Approach - Create a variable called max and initialize it with the value of 
# the first element in the array. Use a for loop to iterate through the rest of 
# the elements in the array.

# 2) Optimal Approach -

arr = [5,8,2,3,7,1,20,10] 
largest = arr[0]

for i in arr:
    if largest < i:
        largest = i

print(largest)