# Check if the given String is Palindrome or not

# Problem Statement: Given a string, check if the string is 
# palindrome or not. A string is said to be palindrome if 
# the reverse of the string is the same as the string.

# Author - Rajiv Das
# Date - 23-08-2026
# ----------------------------------------------------------

# We will discuss 2 approaches - 

# 1)Iterative 2 pointer approach - We know this already! O(n) time and O(1) space complexity.
# 2)Recursive approach - O(n) time and O(n) space complexity.


# Iterative 2 pointer approach -
'''
s = "racecar"
i = 0
j = len(s) - 1
ans = True

while i < j:
    if s[i] != s[j]:
        ans = False
        break
    
    i += 1
    j -= 1

if ans:
    print("String is palindrome")
else:
    print("String is not palindrome")
'''

# 2)Recursive approach -

def palindrome(s, i, j):
    if i >= j:
        return True
    if s[i] == s[j]:
        return palindrome(s, i + 1, j - 1)

    return False
    
s = "racecar"
print(palindrome(s, 0, len(s)-1))