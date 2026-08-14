# Union of Two Sorted Arrays

# Problem Statement - Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays. 
# The union of two arrays can be defined as the common and distinct elements in the two arrays.
# Elements in the union should be in ascending order.

# Author - Rajiv Das
# Date - 14-08-2026
# ----------------------------------------------------------

# There are 3 approaches -

# Approach 1- Using Map :- Our aim is to find the common elements in arr1 and arr2, and the distinct 
# elements of arr1,arr2. Use a Single map to find the frequencies of elements in arr1 and arr2. As we 
# are using only a single map the common element in arr1 and arr2 are treated as a single element for 
# finding frequency, so there would be no duplicates.

# Approach 2- Using Set :- Using a set we can find the distinct elements because the set does not 
# hold any duplicates. Hence we can find the union of arr1 and arr2.

# Optimal Approach - Two Pointers :-


# Approach 1- Using Map :- Time complexity: O((n+m) log(n+m)), Space comp: O(n+m) [ALL IN WORST CASE]
'''
freq = {}
arr1 = [1,2,3,4,5,6,7,8,9,10]
arr2 = [2,3,4,4,5,11,12]

for i in arr1:
    freq[i] = freq.get(i, 0) + 1

for i in arr2:
    freq[i] = freq.get(i, 0) + 1

union = sorted(freq.keys())
print(union)'''


# Approach 2- Using Set :- Time complexity: O((n+m) log(n+m)), Space comp: O(n+m) [ALL IN WORST CASE]
'''
arr1 = [1,3,4,5,6,7,8,9,10]
arr2 = [2,3,4,4,5,11,12]
s = set()

for i in arr1:    # s = set(arr1) | set(arr2)  [Union of two sets] WE CAN WRITE LIKE THIS ALSO IN ONE 
    s.add(i)      # LINE, WHICH WILL DO THIS WHOLE LOOP THING.

for i in arr2:
    s.add(i)

union = sorted(s) #SORTED FUNCTION WILL ALWAYS RETURN A LIST.
print(union)'''


# Optimal Approach - Two Pointers :-  Time Complexity = O(n + m). 
arr1 = [1,3,4,5,6,7,8,9,10]  # Space Complexity: Ignoring the output array: Extra Space = O(1) 
arr2 = [2,3,4,4,5,11,12]     # If the interviewer counts the output array: Space Complexity = O(n + m)
i = j = 0
union = []

while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        if len(union) == 0 or union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1

    elif arr2[j] < arr1[i]:
        if len(union) == 0 or union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1

    else:
        if len(union) == 0 or union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1
        j += 1

while i < len(arr1):
    if len(union) == 0 or union[-1] != arr1[i]:
        union.append(arr1[i])
    i += 1

while j < len(arr2):
    if len(union) == 0 or union[-1] != arr2[j]:
        union.append(arr2[j])
    j += 1

print(union)