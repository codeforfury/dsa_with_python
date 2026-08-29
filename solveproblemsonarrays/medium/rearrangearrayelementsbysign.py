# Rearrange Array Elements by Sign.

# Problem Statement - Given an array of integers containing an equal number 
# of positive and negative elements, rearrange the array so that positive 
# and negative elements appear alternately, while maintaining 
# their relative order. In other words, the positive elements must 
# remain in the same order as they appeared originally, and the 
# negative elements must also remain in their original order.

# Author - Rajiv Das
# Date - 29-08-2026
# ----------------------------------------------------------

# Two approaches for doing this - 

# 1) Brute Force Approach - Store the positive and negative elements separately 
# while traversing the array. Then place one positive and one negative 
# element alternately into the result array. Because elements are 
# added in the same order in which they were encountered, the 
# relative order of positive and negative elements is preserved.
# Time Complexity: O(n).
# Space Complexity: O(n).


# 2) Optimal Approach - Use two indices and an extra result array.
# p = 0 → points to even indices for positive elements: 0, 2, 4, ...
# n = 1 → points to odd indices for negative elements: 1, 3, 5, ...
# Traverse the original array once.
# If the element is positive, place it at result[p] and increase p by 2.
# If the element is negative, place it at result[n] and increase n by 2.
# This automatically creates the pattern positive, negative, positive, negative...
# Since elements are processed from left to right, their relative order is preserved.
# Time Complexity: O(n).
# Space Complexity: O(n) — extra result array.


# 1) Brute Force Approach -
'''
nums = [1,2,-3,-1,-2,3]
pos = []
neg = []

for i in nums:
    if i >= 0:
        pos.append(i)
    else:
        neg.append(i)

p = n = 0
for i in range(len(nums)):
    if i % 2 == 0:
        nums[i] = pos[p]
        p += 1
    else:
        nums[i] = neg[n]
        n += 1

print(nums)'''


# 2) Optimal Approach - 
nums = [1,2,-3,-1,-2,3]
result = [0] * len(nums)
p = 0
n = 1

for i in nums:
    if i >= 0:
        result[p] = i
        p += 2
    else:
        result[n] = i
        n += 2
    
print(result)