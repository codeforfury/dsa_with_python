# Longest Common Prefix.

# Problem Statement - Given an array of strings, find the longest common prefix shared by all the strings. 
# If there is no common prefix, return an empty string "".

# Author - Rajiv Das
# Date - -09-2026
# ----------------------------------------------------------

# Approach for doing this - 

# 1) Optimal Approach - Compare each character position of the first string with the same position in every other string.
# The outer loop selects the character position, while the inner loop checks that position in all strings.
# If a string is shorter or any character is different, stop because the common prefix ends there.
# If all strings have the same character, add that character to the answer.
# Continue until a mismatch is found or the first string ends.
# Time Complexity: O(N × M).
# Space Complexity: O(1).


# 1) Optimal Approach - Vertical Scanning.

strs = ["flower", "flow", "flight"]
ans = ""

# Check each character position of the first string
for i in range(len(strs[0])):
    matched = True

    # Compare the same character position with every string
    for j in range(len(strs)):

        # If the current string is shorter, common prefix ends here
        if i >= len(strs[j]):
            matched = False
            break

        # If characters at the same position are different, stop checking
        if strs[0][i] != strs[j][i]:
            matched = False
            break

    # If the character matched in all strings, add it to the answer
    if matched:
        ans += strs[0][i]
    else:
        # Stop because the common prefix ends at this position
        break

print("If common prefix is there then it is:", ans)