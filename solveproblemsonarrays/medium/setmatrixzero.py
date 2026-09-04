# Set matrix zero.

# Problem Statement - Given an m × n integer matrix, if an element in 
# the matrix is 0, set its entire row and entire column to 0. 
# The operation must be performed in-place, meaning the matrix 
# should be modified without creating another matrix of the same size.

# Author - Rajiv Das
# Date - 05-09-2026
# ----------------------------------------------------------

# Two approaches for doing this - 

# 1) Brute Force Approach - Traverse the entire matrix and whenever a 0 is found, mark all
# non-zero elements in its row and column as -1.
# The -1 acts as a temporary marker so that newly marked cells are
# not treated as original zeroes during the traversal.
# After completing the traversal, convert all -1 markers into 0.
# Time Complexity: O((m × n) × (m + n)).
# Space Complexity: O(1).
# Note: This approach assumes -1 is not a valid value in the input matrix.


# 2) Optimal Approach - Use the first row and first column as markers to remember
# which rows and columns need to be converted to 0.
# Handle the first row and first column separately because
# they are being used to store the markers.
# Time Complexity: O(m × n).
# Space Complexity: O(1).


# 1) Brute Force Approach -
'''
matrix = [ [1, 1, 1], 
           [1, 0, 1], 
           [1, 1, 1] 
         ]

# Get the number of rows and columns in the matrix
row = len(matrix)
column = len(matrix[0])

# Traverse through every element of the matrix
for i in range(row):
    for j in range(column):

        # If the current element is 0, its entire row and column
        # need to be converted to 0
        if matrix[i][j] == 0:

            # Mark all non-zero elements in the current row as -1
            # We use -1 as a temporary marker instead of directly using 0
            for c in range(column):
                if matrix[i][c] != 0:
                    matrix[i][c] = -1

            # Mark all non-zero elements in the current column as -1
            for r in range(row):
                if matrix[r][j] != 0:
                    matrix[r][j] = -1

# After finding all original 0s, convert every -1 marker into 0
for i in range(row):
    for j in range(column):
        if matrix[i][j] == -1:
            matrix[i][j] = 0

# Print the final matrix
print(matrix)'''


# 2) Optimal Approach - 
matrix = [ [1,  2,  3,  4],
           [5,  6,  0,  8],
           [9,  10, 11, 12],
           [13, 14, 15, 16]
         ]

# Get the number of rows and columns in the matrix
row = len(matrix)
column = len(matrix[0])

# These variables remember whether the first row
# or first column originally contains a 0
first_row_zero = False
first_column_zero = False

# Check whether the first row contains a 0
for j in range(column):
    if matrix[0][j] == 0:
        first_row_zero = True
        break

# Check whether the first column contains a 0
for i in range(row):
    if matrix[i][0] == 0:
        first_column_zero = True
        break

# Find 0s in the remaining part of the matrix
# and use the first row and first column as markers
for i in range(1, row):
    for j in range(1, column):
        if matrix[i][j] == 0:

            # Mark this row by putting 0 in its first column
            matrix[i][0] = 0

            # Mark this column by putting 0 in its first row
            matrix[0][j] = 0

# Use the markers to convert the required rows and columns to 0
for i in range(1, row):
    for j in range(1, column):

        # If the row or column has a marker, make the current cell 0
        if matrix[i][0] == 0 or matrix[0][j] == 0:
            matrix[i][j] = 0

# If the first row originally contained 0,
# convert the entire first row to 0
if first_row_zero:
    for j in range(column):
        matrix[0][j] = 0

# If the first column originally contained 0,
# convert the entire first column to 0
if first_column_zero:
    for i in range(row):
        matrix[i][0] = 0

# Print the final matrix
print(matrix)