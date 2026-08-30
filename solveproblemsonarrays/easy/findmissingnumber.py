# Find the Missing Number :- 

# Problem Statement - Given an array arr[] of size n-1 with distinct integers in the range of [1, n]. This array represents a 
# permutation of the integers from 1 to n with one element missing. Find the missing element in the array. 

# Author - Rajiv Das
# Date - 14-08-2026
# ----------------------------------------------------------

# There are 4 approaches :-

# 1) [Naive Approach] Linear Search for Missing Number - O(n^2) Time and O(1) Space
# This approach iterates through each number from 1 to n (where n is the size of the array + 1) and checks if the 
# number is present in the array. For each number, it uses a nested loop to search the array. If a number is not 
# found, it is returned as the missing number. 

# 2) [Better Approach] Using Hashing - O(n) Time and O(n) Space
# This approach uses a hash array (or frequency array) to track the presence of each number from 1 to n in the 
# input array. It first initializes a hash array to store the frequency of each element. Then, it iterates through 
# the hash array to find the number that is missing (i.e., the one with a frequency of 0).

# 3) [Expected Approach 1] Using Sum of n terms Formula - O(n) Time and O(1) Space
# The sum of the first n natural numbers is given by the formula (n * (n + 1)) / 2. The idea is to compute this sum 
# and subtract the sum of all elements in the array from it to get the missing number.

# 4) [Expected Approach 2] Using XOR Operation - O(n) Time and O(1) Space
# XOR of a number with itself is 0 i.e. x ^ x = 0 and the given array arr[] has numbers in range [1, n]. This 
# means that the result of XOR of first n natural numbers with the XOR of all the array elements will be the 
# missing number. To do so, calculate XOR of first n natural numbers and XOR of all the array arr[] elements, and 
# then our result will be the XOR of both the resultant values.


# 1) [Naive Approach] Linear Search for Missing Number - O(n^2) Time and O(1) Space -
'''
arr = [8, 2, 4, 5, 3, 7, 1, 9]

for i in range(1, len(arr)+2):
    found = False
    for j in arr:
        if j == i:
            found = True
            break

    if not found:
        print("Missing Element", i)
        break'''


# 2) [Better Approach] Using Hashing - O(n) Time and O(n) Space
'''
arr = [8, 2, 4, 5, 3, 7, 1]
hash = [0] * (len(arr) + 2)

for i in arr:
    hash[i] = 1

for i in range(1, len(hash)):
    if hash[i] == 0:
        print("Missing number is: ", i)
        break'''


# 3) [Expected Approach 1] Using Sum of n terms Formula - O(n) Time and O(1) Space
'''
arr = [8, 2, 4, 5, 3, 7, 1]
n = len(arr) + 1

expectedsum = n * (n+1) // 2
totalsum = sum(arr)

result = expectedsum - totalsum
print("Missing number:", result)'''


# 4) [Expected Approach 2] Using XOR Operation - O(n) Time and O(1) Space
arr = [8, 2, 4, 5, 3, 7, 1]
xor1 = 0
xor2 = 0

for i in range(len(arr)):
    xor1 = xor1 ^ (i+1)
    xor2 = xor2 ^ arr[i]

xor1 = xor1 ^ (len(arr) + 1)
result = xor1 ^ xor2
print("Missing number:",result)