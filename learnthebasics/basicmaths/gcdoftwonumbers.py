# Problem Statement - You are given two integers n1 and n2. You need find the 
# Greatest Common Divisor (GCD) of the two given numbers. Return the GCD of the two 
# numbers. The Greatest Common Divisor (GCD) of two integers is the largest positive 
# integer that divides both of the integers.

# Author - Rajiv Das
# Date - 11-08-2026

# REMOVE THE COMMENT LINES TO APPLY THE APPROACH.

# ----------------------------------------------------------

#1) First we do the brute force approach i.e looping from 1 to min of both the no.
'''
n1 = 12
n2 = 12
gcd = 1

for i in range(1, min(n1,n2)+1):
    if n1 % i == 0 and n2 % i == 0:
        gcd = i
print(gcd)'''


#2) Now we do a better approach enhancing the first method only 
# i.e looping from min of both the no. till 1. This helps in reducing the no. of iterations.
'''
n1 = 45
n2 = 90
gcd = 1

for i in range(min(n1,n2), 0, -1):
    if n1 % i == 0 and n2 % i == 0:
        gcd = i
        break
print(gcd)'''


#3) Lastly we do the optimal approach i.e the Euclidean Algorithm.
#The Euclidean Algorithm is a method for finding the greatest common divisor (GCD)
#of two numbers. It operates on the principle that the GCD of two numbers remains
#the same even if the smaller number is subtracted from the larger number.
#To find the GCD of n1 and n2 where n1 > n2:
#1. Repeatedly subtract the smaller number from the larger number until one of them becomes 0.
#2. Once one becomes 0, the other is the GCD of the original numbers.

n1 = 90
n2 = 45  
gcd = 1

while (n1 > 0 and n2 > 0):
    if n1 > n2:
        n1 = n1 % n2
    else:
        n2 = n2 % n1

if n1 == 0:
    print(n2)
else:
    print(n1)