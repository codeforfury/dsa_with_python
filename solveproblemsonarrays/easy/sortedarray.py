# Problem Statement - Check if an Array is Sorted (IN ASCENDING ORDER).
# Author - Rajiv Das
# Date - 12-08-2026
# ----------------------------------------------------------

# There are 2 approaches :-

# 1) Brute force approach - We will start with the element at the 0th index, and will 
# compare it with all of its future elements that are present in the array.If the 
# picked element is smaller than or equal to all of its future values then we will 
# move to the next Index/element until the whole array is traversed.If any of the 
# picked elements is greater than its future elements, Then simply we will return 
# False.If the size of the array is Zero or One i.e ( N = 0 or N = 1 ) or the entire 
# array is traversed successfully then we will simply return True.

# 2) Optimal Approach - As we know that for a sorted array the previous of every 
# element is smaller than or equal to its current element.So, Through this, we can 
# conclude that if the previous element is smaller than or equal to the current 
# element then. Then we can say that the two elements are sorted. If the condition is 
# true for the entire array then the array is sorted.We will check every element with 
# its previous element if the previous element is smaller than or equal to the current
# element then we will move to the next index.If the whole array is traversed 
# successfully or the size of the given array is zero or one (i.e N = 0 or N = 1). 
# Then we will return True else return False.

# 1) Brute force approach - Time Complexity: O(N2), as it uses two nested loops to 
                            # compare every pair of elements in the array.
                            #Space Complexity: O(1), as no extra space is used apart 
                            # from a few variables.
'''
arr = [5,8,2,3,7,1,20,10] 
sorted = True

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[j] < arr[i]:
            sorted = False
            break
    if not sorted:
        break

if sorted:
    print("Array is sorted")
else:
    print("Array is not sorted")'''


# 2) Optimal Approach - Time Complexity: O(N), as it checks each adjacent pair once 
                        # in a single pass through the array.
                        #Space Complexity: O(1), as it uses constant extra space 
                        # regardless of input size.
arr = [5,8,2,3,7,1,20,10] 
sorted = True

for i in range(len(arr)-1):
    if arr[i+1] < arr[i]:
        sorted = False
        break

if sorted:
    print("Array is sorted")
else:
    print("Array is not sorted") 