"""
Assignment No.: 2
Course: PROG12974
Name: Prajwal Nautiyal
Sheridan Student Number: 991662442
Submission date:
Instructor's name: Syed Tanbeer
A module file to store the functions used in the menu program
"""

# Function to calculate the power of a number with help of recursion
def power(a,b) -> float:
    if b == 0:
        return 1
    else:
        return a * power(a,b-1)

# Function to calculate the factorial of a number with help of recursion    
def factorial(n) -> float:
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Function to calculate the factorial power series    
def series(n) -> float:
    if n == 1:
        return 1
    else:
        return (power(n,n)/factorial(n)) + series(n-1)