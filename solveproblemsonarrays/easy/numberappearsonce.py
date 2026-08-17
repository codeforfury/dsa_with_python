# Find the number that appears once, and the other numbers twice.

# Problem Statement - Given a non-empty array of integers arr, every element 
# appears twice except for one. Find that single one.

# Author - Rajiv Das
# Date - 16-08-2026
# ----------------------------------------------------------

# There are 3 approaches :-

# 1) Brute force approach - For every element present in the array, we will do a linear search and 
# count the occurrence. If for any element, the occurrence is 1, we will return it.

# 2) Better Approach - In the previous approach, we were finding the occurrence of an element using 
# linear search. We can optimize this using hashing technique. We can simply hash the elements along 
# with their occurrences in the form of (key, value) pair. Thus, we can reduce the cost of finding 
# the occurrence and hence the time complexity. Now, hashing can be done in two different ways and 
# they are the following: 
# i) Array hashing(not applicable if the array contains negatives or very large numbers) 
# ii) Hashing using the map data structure

# Array Hashing (Frequency Array) is a hashing technique that uses an array (list) to store the 
# frequency of elements. In this method, the array index itself represents the element, and the value 
# stored at that index represents its frequency. It is most efficient when the elements lie within a 
# small, known range because it provides O(1) access time. However, it cannot directly handle 
# negative numbers and may waste memory if the maximum element is very large, since memory must be 
# allocated for every index up to the maximum value, even if many indices are never used.

# A Hash Map (Dictionary) is a hashing technique that stores data in the form of key-value pairs, 
# where the key represents the element and the value represents its frequency or associated data. It 
# stores only the elements that are actually present in the input, making it memory-efficient when 
# the range of values is large or unknown. A hash map can handle negative numbers, large integers, 
# strings, and other hashable data types. The average time complexity for insertion, deletion, and 
# searching is O(1).

# 3) Optimal Approach - We will just perform the XOR of all elements of the array using a loop and 
# the final XOR will be the answer.

# 1) Brute force approach - Time comp: O(n^2), Space comp: O(1).
'''
arr = [1,3,7,6,7,1,6]
c = 0
for i in arr:
    for j in arr:
        if j == i:
            c += 1

    if c == 1:
        print("Element that appeared once:",i)
        break
    c = 0'''


# 2) Better Approach - Time comp: O(n), Space comp: O(n). We will use map dictionary
'''
arr = [1,3,7,6,7,1,6]
freq = {}

for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

for key, value in freq.items():
    if value == 1:
        print("Element that appeared once:",key)
        break'''


# 3) Optimal Approach - Time comp: O(n), Space comp: O(1)
arr = [1,3,7,6,7,1,6,3,8]
xor = 0
for i in arr:
    xor = xor ^ i

print("Element that appeared once:",xor)