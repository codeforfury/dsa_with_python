# Search Single Element in a sorted array.

# Problem Statement - Given a sorted array of integers in which every 
# element appears twice except one element, which appears only once, 
# find and return the single element.

# Author - Rajiv Das
# Date - 29-08-2026
# ----------------------------------------------------------

# Two approaches for doing this - 

# 1) Brute Force Approach - Traverse the sorted array and compare 
# adjacent elements. Since every element appears twice except one, 
# the single element is the one that does not have an equal adjacent pair.
# Time: O(n)
# Space: O(1)

# 2) Optimal Approach - Use binary search on the pairing pattern. 
# Before the single element, pairs start at even indices; after the 
# single element, this pattern shifts. Make mid even and compare 
# nums[mid] with nums[mid + 1]. If they are equal, search to the right; 
# otherwise, search at mid or to the left. When low == high, 
# that position contains the single element.
# Time: O(log n)
# Space: O(1)


# 1) Brute Force Approach -
'''
nums = [1,1,2,2,3,3,4,4,5,5,6]

for i in range(0, len(nums)-1, 2):
    if nums[i] != nums[i+1]:
        print("The no. that appeared once:", nums[i])
        break
else:
    print("The no. that appeared once:", nums[-1])'''


# 2) Optimal Approach -
nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]
low = 0
high = len(nums) - 1

while(low < high):
    mid = (low + high) // 2

    # Make mid even so that mid and mid+1 form a pair.
    if mid % 2 != 0:
        mid -= 1

    # If the pair is correct, the single element is on the right.
    if nums[mid] == nums[mid + 1]:
        low = mid + 2

    # If the pair is broken, the single element is at mid or on the left.
    else:
        high = mid

# When low == high, nums[low] is the single element.
print("The no. that appeared once:", nums[low])