# Max and Min ASCII Sum of Strings.

# Problem Statement - Given an array of N strings, calculate the sum of ASCII values 
# of all characters in each string. Find and print the string having the 
# minimum ASCII sum and the string having the maximum ASCII sum.

# Author - Rajiv Das
# Date - 12-09-2026

# ----------------------------------------------------------

# Approach for doing this -

# 1) Optimal Approach - Traverse each string and calculate the total ASCII value of its characters.
# Keep track of the minimum and maximum ASCII sums along with their corresponding strings.
# For every string, add the ASCII value of each character to calculate its total sum.
# If the current sum is smaller than the minimum sum, update the minimum string.
# If the current sum is greater than the maximum sum, update the maximum string.
# After checking all strings, print the string with the minimum ASCII sum followed by the string with the maximum ASCII sum.
# Time Complexity: O(N × M), where N is the number of strings and M is the average length of a string.
# Space Complexity: O(1).


# 1) Optimal Approach - 
n = 4
strings = ["cat", "dog", "a", "hello"]
maxsum = float('-inf')
minsum = float('inf')

for i in range(n):
    s = 0
    for char in strings[i]:
        s += ord(char)

    if s > maxsum:
        maxsum = s
        max_ascii = strings[i]
    if s < minsum:
        minsum = s
        min_ascii = strings[i]

print(min_ascii, max_ascii)