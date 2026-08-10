# Problem Statement - Given an array arr of n elements. The task is to reverse the 
# given array. The reversal of array should be inplace.

# Author - Rajiv Das
# Date - 09-08-2026
# ----------------------------------------------------------

arr = [5,7,3,4,1,0,6]
i = 0
j = len(arr) - 1
temp = 0

while(i < j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

    i += 1
    j -= 1

print(arr)