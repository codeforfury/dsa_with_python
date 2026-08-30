# Find Peak element in an array.

# Problem Statement - Given an array of integers, find the index of any 
# peak element. A peak element is an element that is greater 
# than its adjacent (both left and right) elements. If there are multiple peak 
# elements, return the index of any one of them.

# Author - Rajiv Das
# Date - 30-08-2026
# ----------------------------------------------------------

# Two approaches for doing this - 

# 1) Brute Force Approach - Traverse the array and check each element to determine 
# whether it is greater than its adjacent elements. If a peak element 
# is found, return its index. If there are multiple peak elements, 
# return the index of any one of them.
# Time: O(n)
# Space: O(1)

# 2) Optimal Approach - Use Binary Search by comparing nums[mid] with 
# nums[mid + 1]. If nums[mid] < nums[mid + 1], a peak must exist 
# on the right side, so move low to mid + 1. Otherwise, 
# a peak exists at mid or on the left side, so move high to mid. 
# When low == high, that index is a peak element.
# Time: O(log n)
# Space: O(1)


# 1) Brute Force Approach -
'''
nums = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]

# Check the first element
if nums[0] > nums[1]:
    print("The index of Peak element is:", 0)

# Check the last element
elif nums[-1] > nums[-2]:
    print("The index of Peak element is:", len(nums) - 1)

# Check the elements between the first and last
else:
    for i in range(1, len(nums) - 1):

        # Check if the current element is greater than both neighbors
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            print("The index of Peak element is:", i)
            break

    else:
        print("There is no peak element.")'''


# 2) Optimal Approach -
nums = [1, 2, 3, 4, 5, 7, 8, 5, 1]

low = 0
high = len(nums) - 1

while(low < high):
    mid = (low + high) // 2

    # If the array is increasing at mid,
    # a peak must exist on the right side
    if nums[mid] < nums[mid + 1]:
        low = mid + 1

    # If the array is decreasing at mid,
    # a peak exists at mid or on the left side
    else:
        high = mid

# When low == high, we have reached a peak element
print("The index of Peak element is:", low)


# Peak Element — Approach Selection
# If duplicates are NOT allowed: Use Binary Search → O(log n).
# If duplicates ARE allowed: For a strict peak (> both neighbors), use Brute Force → O(n).
# Remember: For Peak Element, check whether duplicates are allowed first.