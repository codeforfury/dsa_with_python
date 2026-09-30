# String to Integer (atoi).

# Problem Statement - Given a string s, convert it to a 32-bit signed integer.
# Ignore leading whitespace, check for an optional '+' or '-' sign, and read
# consecutive digits until a non-digit character is encountered. If the result
# is outside the 32-bit signed integer range, clamp it to the nearest limit.

# Author - Rajiv Das
# Date - 30-09-2026

# ----------------------------------------------------------

# Approach for doing this -

# 1) Optimal Approach - First skip all leading spaces and check for an optional
# '+' or '-' sign. Then skip leading zeroes and traverse the remaining characters
# to calculate the integer value using the formula (ans * 10) + digit.
# Stop when a non-digit character is encountered.
# Apply the sign to the calculated number.
# Finally, check whether the result is outside the 32-bit signed integer range
# and clamp it to -2147483648 or 2147483647 if necessary.
# Time Complexity: O(N), where N is the length of the string.
# Space Complexity: O(1).


# 1) Optimal Approach -
s = " -0002147-483640afgdd"

ans = 0
sign = 1
i = 0

# Skip leading spaces
while i < len(s):

    if s[i] == ' ':
        i += 1
    else:
        break

# Check sign
if i < len(s) and s[i] == '-':
    sign = -1
    i += 1

elif i < len(s) and s[i] == '+':
    i += 1

# Skip leading zeroes
while i < len(s):

    if s[i] == '0':
        i += 1
    else:
        break

# Read remaining digits
while i < len(s):

    a = ord(s[i]) - ord('0')

    if a >= 0 and a <= 9:
        ans = (ans * 10) + a
    else:
        break

    i += 1

ans = ans * sign

# Check whether it is in 32-bit range
if ans < -2147483648:
    print(-2147483648)

elif ans > 2147483647:
    print(2147483647)

else:
    print(ans)