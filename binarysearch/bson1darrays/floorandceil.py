# Floor and Ceil in Sorted Array.

# Problem Statement - Given a sorted array of integers and a target 
# value x, find the floor and ceiling of x.
# Floor: Largest element ≤ x
# Ceiling: Smallest element ≥ x

# Author - Rajiv Das
# Date - 25-08-2026
# ----------------------------------------------------------

# Two approaches for doing this - 

# 1) Brute Force Approach - Traverse the sorted array and keep track of 
# the largest element ≤ x as the floor and the smallest element ≥ x as 
# the ceiling. Update the floor when a larger valid element is found 
# and the ceiling when a smaller valid element is found.
# Time: O(n)
# Space: O(1)

# 2) Optimal Approach - Since the array is sorted, use Binary Search. 
# If nums[mid] >= x, store mid as a possible answer and search the left half 
# for a smaller valid index. Otherwise, search the right half. 
# Initialize ans = -1 to indicate that no valid index has been found.
# Time: O(log n)
# Space: O(1)


# 1) Brute Force Approach -
'''
nums = [3, 4, 4, 7, 8, 10]
x = 5

for i in range(len(nums)-1, -1, -1):
    if nums[i] <= x:
        floor = nums[i]
        break

for i in range(len(nums)):
    if nums[i] >= x:
        ceil = nums[i]
        break

print("The floor is:", floor)
print("The ceilling is:", ceil)'''
    
        
# 2) Optimal Approach -
nums = [3, 4, 4, 7, 8, 10]
x = 5
low = 0
high = len(nums) - 1

# FOR FINDING FLOOR VALUE
while(low <= high):
    mid = (low + high) // 2
    if nums[mid] <= x:
        floor = nums[mid]
        low = mid + 1

    else:
        high = mid - 1

# FOR FINDING CEILLING VALUE
low = 0
high = len(nums) - 1

while(low <= high):
    mid = (low + high) // 2
    if nums[mid] >= x:
        ceil = nums[mid]
        high = mid - 1

    else:
        low = mid + 1

print("The floor is:", floor)
print("The ceilling is:", ceil)