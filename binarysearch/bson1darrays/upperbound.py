# Implement Upper Bound.

# Problem Statement - Given a sorted array of N integers and an integer x, 
# write a program to find the upper bound of x. The upper bound algorithm 
# finds the first or the smallest index in a sorted array where the value 
# at that index is greater than the given key i.e. x. The upper bound is 
# the smallest index, ind, where arr[ind] > x.

# Author - Rajiv Das
# Date - 25-08-2026
# ----------------------------------------------------------

# Two approaches for doing this - 

# 1) Brute Force Approach - Loop through the array using i. If nums[i] > x, 
# print i and stop using break. Since the array is sorted and we check from the 
# beginning, the first matching index is the upper bound. If no element 
# satisfies the condition, the for...else block prints that no 
# smallest index was found.
# Time: O(n)
# Space: O(1)

# 2) Optimal Approach - Since the array is sorted, use Binary Search to find the 
# smallest index where nums[i] > x. If nums[mid] > x, store mid as a 
# possible answer and search the left half; otherwise, search the right half. 
# Initialize ans = -1 to indicate that no valid index was found.
# Time: O(log n)
# Space: O(1)


# 1) Brute Force Approach -
'''
nums = [3,5,8,15,19]
x = 9

for i in range(len(nums)):
    if nums[i] > x:
        print("The smallest index is:", i)
        break

else:
    print("No smallest index found")'''


# 2) Optimal Approach -
nums = [3,5,8,9,15,19]
x = 9
ans = -1
low = 0
high = len(nums) - 1

while(low <= high):
    mid = (low + high) // 2

    if nums[mid] > x:
        ans = mid
        high = mid - 1

    else:
        low = mid + 1

if ans == -1:
    print("No smallest index found")
else:
    print("The smallest index is:", ans)