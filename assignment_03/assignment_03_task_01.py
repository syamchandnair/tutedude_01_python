# Assignment 3:
# Module 4: Functions & Modules in Python
# Task 1: Calculate Factorial Using a Function

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

vNumber=int(input("Enter a number: "))
print('Factorial of', vNumber, 'is:', factorial(vNumber))

