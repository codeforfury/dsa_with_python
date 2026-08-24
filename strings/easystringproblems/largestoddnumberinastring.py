# Largest Odd Number in a String.

# Problem Statement - Given a string s, representing a large integer, the task is 
# to return the largest-valued odd integer (as a string) that is a 
# substring of the given string s. The number returned should not have 
# leading zero's. But the given input string may have leading zero.

# Author - Rajiv Das
# Date - 24-08-2026
# ----------------------------------------------------------


str = "0057234"
index = -1

for i in range(len(str) - 1, -1, -1):
    if int(str[i]) % 2 != 0:
        index = i
        break

if index == -1:
    print("No odd number found")
else:
    j = 0
    while j < index:
        if int(str[j]) != 0:
            break
        j += 1

    print(str[j:index+1])