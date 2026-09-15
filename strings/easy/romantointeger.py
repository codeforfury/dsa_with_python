# Roman to Integer.

# Problem Statement - Given a string s representing a Roman numeral, 
# convert it into its corresponding integer value. Roman numerals use 
# the following symbols:
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000
#When a smaller value appears before a larger value, it is subtracted instead of added.

# Author - Rajiv Das
# Date - 15-09-2026
# ----------------------------------------------------------

# Approach for doing this - 

# 1) Optimal Approach -
# Store the value of each Roman symbol in a dictionary.
# Traverse the string from left to right and compare the current symbol with the next symbol.
# If the current value is smaller than the next value, subtract the current value.
# Otherwise, add the current value to the total.
# This handles subtraction cases such as IV, IX, XL, XC, CD, and CM.
# Continue until all Roman symbols are processed.
# Time Complexity: O(N).
# Space Complexity: O(1).


# 1) Optimal Approach - 
roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
s = "MCMXLIV"
ans = 0

for i in range(len(s)):
    if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
        ans -= roman[s[i]]

    else:
        ans += roman[s[i]]

print(ans)