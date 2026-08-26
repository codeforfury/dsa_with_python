# Count Occurrences in Sorted Array.

# Problem Statement - You are given a sorted array containing N integers 
# and a number X, you have to find the occurrences of X in the given array.

# Author - Rajiv Das
# Date - 26-08-2026
# ----------------------------------------------------------

# Two approaches for doing this - 

# 1) Brute Force Approach - Traverse the array and count every element 
# equal to x. Since the array is sorted, we can simply check 
# each element and increment count whenever nums[i] == x.
# Time: O(n)
# Space: O(1)

# 2) Optimal Approach - Use binary search to find the first and last occurrence 
# of x. Then calculate the count using last - first + 1. If x is not found, return 0.
# Time: O(log n)
# Space: O(1)


# 1) Brute Force Approach -
'''
nums = [2, 2 , 3 , 3 , 3 , 3 , 4]
x = 3
c = 0

for i in range(len(nums)):
    if nums[i] == x:
        c += 1

print("The no. of occurence:", c)'''
    
        
# 2) Optimal Approach -
nums = [2, 2 , 3 , 3 , 3 , 3 , 4]
x = 3
findex = 0
lindex = -1
low = 0
high = len(nums) - 1

while(low <= high):
    mid = (low + high) // 2

    if nums[mid] == x:
        findex = mid
        high = mid - 1

    elif nums[mid] < x:
        low = mid + 1

    else:
        high = mid - 1


low = 0
high = len(nums) - 1

while(low <= high):
    mid = (low + high) // 2

    if nums[mid] == x:
        lindex = mid
        low = mid + 1

    elif nums[mid] < x:
        low = mid + 1

    else:
        high = mid - 1

c = lindex - findex + 1
print("The no. of occurence:", c)