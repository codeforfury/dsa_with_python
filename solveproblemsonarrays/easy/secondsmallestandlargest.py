# Problem Statement - Find Second Smallest and Second Largest Element in an array
# Author - Rajiv Das
# Date - 12-08-2026
# ----------------------------------------------------------

# There are 3 approaches :-

# 1) Brute force approach - Sort the array in ascending order.
# The element at the second index (index 1) is the second smallest element.The element 
# at the second index from the end (index length-2) is the second largest element.

# 2) Better Approach - Perform a single traversal to find the smallest and largest 
# elements in the array.After that, traverse the array again to find the element just 
# greater than the smallest element (this will be the second smallest).Similarly, 
# find the element just smaller than the largest element (this will be the second largest).

# 3) Optimal Approach - In one pass only we are calculating all 4 
# elements i.e. largest, second largest, smallest and second smallest. 

# Better Approach - 
'''
arr = [5,8,2,3,7,1,20,10] 
max = arr[0]
min = arr[0]
smax = arr[0]
smin = arr[0]

for i in arr:
    if max < i:
        max = i
    if min > i:
        min = i

for i in arr:
    if smax < i and i != max:
        smax = i
    if smin > i and i != min:
            smin = i

print(smax)
print(smin)'''

# Optimal Approach -

arr = [5,8,2,3,7,1,20,10]
max = arr[0]
min = arr[0]
smax = float('-inf')
smin = float('inf') 

for i in arr:
    if max < i:
        smax = max
        max = i
    elif smax < i and i != max:
        smax = i

    if min > i:
        smin = min
        min = i
    elif smin > i and i != min:
        smin = i

print(smax)
print(smin)