# Assignment 2:
# Module 3: Control Structures in Python
#
# Task 2: Sum of Integers from 1 to 50 Using a Loop

vStartNumber=1
vEndNumber=50
vFinalOutput=0

for i in range(vStartNumber, (vEndNumber+1)):
    vFinalOutput+=i

print('The sum of numbers from', vStartNumber, 'to', vEndNumber, 'is: ', vFinalOutput)
