# Remove Outermost Parentheses.

# Problem Statement - A valid parentheses string is defined by the following rules:
# It is the empty string "".
# If A is a valid parentheses string, then so is "(" + A + ")".
# If A and B are valid parentheses strings, then A + B is also valid.
# A primitive valid parentheses string is a non-empty valid string that cannot 
# be split into two or more non-empty valid parentheses strings. Given a valid 
# parentheses string s, your task is to remove the outermost parentheses from 
# every primitive component of s and return the resulting string.

# Author - Rajiv Das
# Date - 23-08-2026
# ----------------------------------------------------------

#Two approaches for doing this - 
# 1) Brute Force Approach - Stack Approach: Use a stack to keep track 
# of the parentheses. For each (, push it into the stack and add it to the 
# result only if it is not the outermost (. For each ), pop from the stack 
# and add it to the result only if the stack is still not empty. Thus, 
# the outermost pair of every primitive is removed.
# Time Complexity: O(n) 
# Space Complexity: O(n), For using Stack.

# 2) Optimal Approach - Balance Counter Approach: Instead of using a stack, 
# use a balance counter to track the nesting level. 
# For (, add it only when balance > 0, then increase the balance. For ), first 
# decrease the balance, then add it only when balance > 0. This automatically 
# skips the outermost parentheses of every primitive.
# Time Complexity: O(n).
# Space Complexity: O(1).


# 1) Brute Force Approach - Stack Approach
'''
s = "(()())(())"

stack = []
result = ""

for ch in s:

    if ch == '(':

        # Add only if this is NOT the outermost '('
        if len(stack) > 0:
            result += '('

        # Remember this '('
        stack.append('(')

    else:

        # Remove the matching '('
        stack.pop()

        # Add only if this is NOT the outermost ')'
        if len(stack) > 0:
            result += ')'

print(result)'''

# 2) Optimal Approach - Balance Counter Approach
s = "(()())(())"
balance = 0
result = ""

for ch in s:
    if ch == '(':
        # If balance > 0, this is an inner '('
        if balance > 0:
            result += '('

        balance += 1

    else:
        balance -= 1
        # If balance > 0, this is an inner ')'
        if balance > 0:
            result += ')'

print(result)