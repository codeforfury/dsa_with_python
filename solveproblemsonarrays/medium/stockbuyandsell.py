# Best time to buy and sell stock

# Problem Statement - Given an array arr of n integers, where arr[i] represents 
# price of the stock on the ith day. Determine the maximum profit achievable by 
# buying and selling the stock at most once. The stock should be purchased before 
# selling it, and both actions cannot occur on the same day.

# Author - Rajiv Das
# Date - 20-08-2026
# ----------------------------------------------------------

#Two approaches for doing this - 
# 1) Brute Force Approach - We try every possible pair of 
# days (buy day and sell day after buy) and calculate the profit. The maximum 
# profit among all these pairs is our answer. If no profit is possible, return 0. 
# Loop through all days to consider each as a possible buy day. For each buy day, 
# loop through all future days to consider them as sell days. Calculate 
# the profit for each (buy, sell) pair. Track the maximum profit seen.
# Time Complexity: O(n²) Because for each element, we are checking every future element nested loops.
# Space Complexity: O(1) No extra space used, only variables for storing max profit.

# 2) Optimal Approach - Traverse the array once while keeping track of the minimum 
# price seen so far. For each price, calculate the profit obtained by selling at 
# that price and update the maximum profit. Then update the minimum buying price.
# Time Complexity: O(n).
# Space Complexity: O(1).


# 1) Brute Force Approach - 
'''
arr = [7,1,5,3,6,4]
maxprofit = 0

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        profit = arr[j] - arr[i]
        maxprofit = max(maxprofit, profit)

print("Maximum profit is:",maxprofit)'''


# 2) Optimal Approach - 
arr = [7,1,5,3,6,4]
minprice = arr[0]
maxprofit = 0

for i in range(1, len(arr)):
    # Calculate profit if I sell today.
    profit = arr[i] - minprice

    # Find the maximum profit so far.
    maxprofit = max(maxprofit, profit)

    # Update the minimum buying price in every iteration if found.
    minprice = min(minprice, arr[i])

print("Maximum profit is:",maxprofit)