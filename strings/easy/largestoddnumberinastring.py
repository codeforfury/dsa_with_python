# Largest Odd Number in a String.

# Problem Statement - Given a string s, representing a large integer, the task is 
# to return the largest-valued odd integer (as a string) that is a 
# substring of the given string s. The number returned should not have 
# leading zero's. But the given input string may have leading zero.

# Author - Rajiv Das
# Date - 24-08-2026
# ----------------------------------------------------------


str = "0057234"

# Store the index of the rightmost odd digit
index = -1

# Traverse the string from right to left
for i in range(len(str) - 1, -1, -1):

    # Check if the current digit is odd
    if int(str[i]) % 2 != 0:

        # Store the index of the rightmost odd digit
        index = i

        # Stop because we found the largest possible odd number
        break

# If no odd digit is found, no odd number can be formed
if index == -1:
    print("No odd number found")

else:
    # Start from the beginning of the string
    j = 0

    # Skip leading zeroes before the odd number
    while j < index:

        # Stop when a non-zero digit is found
        if int(str[j]) != 0:
            break

        # Move to the next digit
        j += 1

    # Print the substring from the first non-zero digit
    # up to and including the rightmost odd digit
    print(str[j:index+1])