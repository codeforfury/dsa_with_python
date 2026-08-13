# Left Rotate the Array by One.

# Problem Statement - Given an integer array nums, rotate the array to the left by one.
# Author - Rajiv Das
# Date - 13-08-2026
# ----------------------------------------------------------

# There are 2 approaches :-

# 1) Brute force approach - Create a dummy array of the same length as the original array. Shift all elements in 
# the original array toward the left, copying them into the dummy array.After shifting, place the value of the 0th 
# index of the original array into the last element of the dummy array.Finally, print the dummy array which now 
# contains the left-shifted elements with the 0th element moved to the last position.

# 2) Optimal Approach - Store the value of the first element of the array in a temporary variable.Iterate through 
# the array starting from the second element.Shift each element one position to the left by assigning the current 
# element to the position of its predecessor.After completing the iteration, place the value from the temporary 
# variable into the last position of the array.


# 1) Brute force approach - Time and space complexity - O(n).
'''
arr = [2,4,1,10,7,6]
temp = [0]*len(arr)

for i in range(1, len(arr)):
    temp[i-1] = arr[i]
temp[len(arr)-1] = arr[0]

print(temp)'''


# 2) Optimal Approach - Time comp: O(n), Space comp: O(1)
arr = [2,4,1,10,7,6]
temp = arr[0]

for i in range(1, len(arr)):
    arr[i-1] = arr[i]
arr[len(arr)-1] = temp

print(arr)