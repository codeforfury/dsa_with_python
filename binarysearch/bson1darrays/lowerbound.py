# Implement Lower Bound.

# Problem Statement - Given a sorted array of N integers and 
# an integer x, write a program to find the lower bound of x.
# The lower bound algorithm finds the first or the smallest index in a sorted 
# array where the value at that index is greater than or equal to a given 
# key i.e. x. The lower bound is the smallest index, ind, where arr[ind] >= x. But 
# if any such index is not found, the lower bound algorithm returns n i.e. size of 
# the given array.

# Author - Rajiv Das
# Date - 24-08-2026
# ----------------------------------------------------------

# Two approaches for doing this - 

# 1) Brute Force Approach - Check the sorted array from left to right. For each 
# index i, if nums[i] >= x, it is the lower bound, so print i and stop. 
# If no such element is found, report that no lower bound exists.
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
nums = [3,5,8,15,19]
x = 2

for i in range(len(nums)):
    if nums[i] >= x:
        print("The smallest index is:", i)
        break

else:
    print("No smallest index found")'''


# 2) Optimal Approach -
nums = [3,5,8,15,19]
x = 1
ans = -1
low = 0
high = len(nums) - 1

while(low <= high):
    mid = (low + high) // 2

    if nums[mid] >= x:
        ans = mid
        high = mid - 1

    else:
        low = mid + 1

if ans == -1:
    print("No smallest index found")
else:
    print("The smallest index is:", ans)