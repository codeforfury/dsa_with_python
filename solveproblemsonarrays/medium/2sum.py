# Two Sum : Check if a pair with given sum exists in Array

# Problem Statement - Given an array of integers arr[] and an integer target.
# 1st variant: Return YES if there exist two numbers such that their sum is equal to the target. 
# Otherwise, return NO.
# 2nd variant: Return indices of the two numbers such that their sum is equal to the target. 
# Otherwise, we will return {-1, -1}.

# Author - Rajiv Das
# Date - 18-08-2026
# ----------------------------------------------------------

# There are 3 approaches :-

# 1) Brute force approach - For each element of the given array, we will try to search for another 
# element such that its sum is equal to the target. If such two numbers exist, we will return the 
# indices or “YES” accordingly. (Will use nested loop)

# 2) Better Approach - Store each element along with its original index using a tuple: (value, index).
# Sort the list based on the values.
# Use two pointers: i at the beginning and j at the end.
# If nums[i][0] + nums[j][0] < target, increment i.
# If the sum is greater than the target, decrement j.
# If the sum equals the target, return their original indices stored in the tuples.
# If no pair is found, return (-1, -1).

# 3) Optimal Approach - we will store the element along with its index in the HashMap. Thus we can 
# easily retrieve the index of the other element i.e. target (selected element) without iterating the 
# array. We will select the element of the array one by one using a loop (say i). Then we will check 
# if the other required element (i.e. target - arr[i]) exists in the HashMap. If that element exists, 
# we will return the current index i.e. i, and the index of the element found using map i.e. 
# mp[target - arr[i]]. If that element does not exist, then we will just store the current element 
# in the HashMap along with its index. Because in the future, the current element might be a part of 
# our answer. Finally, if we are out of the loop, that means there is no such pair whose sum is equal 
# to the target. In this case, we will return either “NO” or {-1, -1} as per the variant of the question. 


# 1) Brute force approach - Time Complexity: O(N²), Space Complexity: O(1)
'''
nums = [2,6,5,8,11]
target = 14 

def twosum(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] + nums[i] == target:
                return i,j

    return -1,-1

print(twosum(nums))'''


# 2) Better Approach - Time Complexity: O(n log n), Space Complexity: O(n)
'''
nums = [2,6,5,11,8]
nums = [(nums[i], i) for i in range(len(nums))] # List comprehension
target = 17 
nums.sort() # Python sorts tuples according to the first element by default. Sorts the existing list.

def twosum():
    i = 0
    j = len(nums) - 1
    while(i < j):
        if nums[i][0] + nums[j][0] < target:
            i += 1

        elif nums[i][0] + nums[j][0] > target:
            j -= 1

        else:
            return nums[i][1], nums[j][1]

    return -1, -1

print(twosum())'''


# 3) Optimal Approach - Time Complexity: O(n), Space Complexity: O(n)
nums = [2,6,5,8,11]  
target = 17 
hashmap = {}

def twosum():
    for i in range(len(nums)):
        if target - nums[i] in hashmap:
            return hashmap[target - nums[i]], i

        else:
            hashmap[nums[i]] = i

    return -1,-1

print(twosum())