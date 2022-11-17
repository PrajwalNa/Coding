"""
Dev: Prajwal Nautiyal
Last Update: 9 November 2022
A basic calculator program.
!! This program is only meant to be run in the terminal !!
"""

import argparse                     # Importing the argparse module for taking the input from the user
import timeit as ti                 # Importing the timeit module to calculate the runtime of the program

def main():
    start = ti.default_timer()                                      # Starting the timer for the program                                                        # Infinite loop
    num = inp()                                                     # Calling the input function, stores the input in a tuple
    try:
        calT_start = ti.default_timer()                                     # Starting the timer for the calculation
        result = cal(num[0], num[1], num[2])                                # Calling the calculation function
        prnt(num[0], num[1], num[2], result)                                # Calling the output function
        calT_stop = ti.default_timer()                                      # Stopping the timer for the calculation
        print(f"Calculation Time: {(calT_stop - calT_start):.4f} seconds")  # Printing the calculation time
    except Exception as e:                                                  # Exception handling
        print(f"Error: {e}")
    stop = ti.default_timer()                                       # Stopping the timer for the program
    print(f"Total Runtime: {(stop - start):.4f} seconds")           # Printing the total runtime of the program

def inp():
    # using argparse to take the input from the user
    parser = argparse.ArgumentParser(description="A basic calculator program. The available operators are '+', '-', '*', '/', '**', '%")
    parser.add_argument("-n", "--num", type = float, dest = "number", nargs = 2, help = "Argument to store enter two numbers", required = True)
    parser.add_argument("-o", "--operator", type = str, dest = "operator", help = "Argument to store the operator", required = True)
    args = parser.parse_args()      # Parsing the arguments
    a, b = args.number              # Storing the numbers in a and b
    ops = args.operator             # Storing the operator in ops
    return a, b, ops

def cal(num1 : float, num2 : float, op : str) -> float:             # Defining the calculation function, type casting is used; takes two numbers and an operator as argument
    match op:                       # Using the match statement to match the operator
        case '+':
            val = num1 + num2
        case '-':
            val = num1 - num2
        case '*':
            val = num1 * num2
        case '/':
            val = num1 / num2
        case '**':
            val = num1 ** num2
        case '%':
            val = num1 % num2
        case _:
            val = 0.0
    return val

def prnt(n1, n2, opr, valu):        # Defining the output function, takes the two inputs, the chosen operator and the result as argument
    print(f"The expression {n1}{opr}{n2} has result {valu}")

if __name__ == "__main__":          # Source Control
    main()                          # Calling the main function