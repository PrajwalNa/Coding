"""
Dev: Prajwal Nautiyal
Last Update: 8 November 2022
Simple area calculator for a Rectangle/Square with a bonus of circle
"""

import math
import timeit as ti
from calculator import cal as c                     # Basic Calculator Function
from func import ent as userin                      # Reusing the function to take input from user from another module

def main():
    start = ti.default_timer()                                                      # Start the timer
    dimen1, dimen2 = uin()                                                          # user inputs for the dimensions of rectangle
    output = arr_rad(dimen1, dimen2)                                                # calling main calculation function
    result(dimen1, dimen2, output[0], output[1], output[2], output[3])              # print the results
    stop = ti.default_timer()                                                       # Stop the timer
    print(f"Runtime: {stop - start} seconds")                                       # Print the runtime

def uin():                                          # user input function
    print("Enter Values for the dimensions of Rectangle: ")
    a, b = userin()
    return a, b

def arr_rad(l : float, b : float):                  # function to calculate the area & perimeter for the rectangle along with radius, area of circle whose circumference is equal to perimeter of rectangle
    area = c(l, b, '*')                             # calling the basic calculator function to calculate the area of rectangle
    perimeter = c(2*l, 2*b, '+')                    # calling the basic calculator function to calculate the perimeter of rectangle
    radius = c(perimeter, 2*math.pi, '/')           # calling the basic calculator function to calculate the radius of circle using the perimeter of rectangle as circumference
    ar_cir = c(radius*radius, 2*math.pi, '*')       # calling the basic calculator function to calculate the area of circle
    return area, perimeter, radius, ar_cir          # returning the values

def result(n1 , n2, ar, pr, rd, arc):               # function to print the results
    print(f"\nThe rectangle with dimenions {n1} x {n2} has,\
        \nArea = {ar} unit sq.\nPerimeter = {pr} units\
        \nAnd if the perimeter was equal to the circumference of a circle the approximate radius would be = {rd:.2f} units\
        \nThe are of circle with approximate radius = {rd:.2f} units would be approx {arc:.2f} unit sq.")

if __name__ == "__main__":                          # main function
    main()
