# Search Insert Position.

# Problem Statement - Given a sorted array of distinct integers and a target 
# value x, find the index of x. If x is not present, return the index 
# where x should be inserted so that the array remains sorted.

# Author - Rajiv Das
# Date - 25-08-2026
# ----------------------------------------------------------

# Two approaches for doing this - 

# 1) Brute Force Approach - Check the sorted array from left to right. For each 
# index i, if nums[i] >= x, it is the lower bound, so print i and stop. 
# If no such element is found, report that no lower bound exists.
# Time: O(n)
# Space: O(1)

# 2) Optimal Approach - Since the array is sorted, use Binary Search. 
# If nums[mid] >= x, store mid as a possible insertion position 
# and search the left half; otherwise, search the right half. 
# Initialize ans = len(nums) so that if x is greater than every element, 
# the insertion position is at the end of the array.
# Time: O(log n)
# Space: O(1)


# 1) Brute Force Approach -
'''
nums = [3,5,8,15,19]
x = 20

for i in range(len(nums)):
    if nums[i] == x:
        print("Found at index:", i)
        break
        
    if nums[i] > x:
        print("Not found, should be at index:", i)
        break
else:
    print("Not found, should be at index:", len(nums))'''


# 2) Optimal Approach -
nums = [3,5,8,15,19]
x = 17
ans = len(nums)
low = 0
high = len(nums) - 1

while(low <= high):
    mid = (low + high) // 2

    if nums[mid] >= x:
        ans = mid
        high = mid - 1

    else:
        low = mid + 1

print("Found at index:", ans)