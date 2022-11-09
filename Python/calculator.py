"""
Dev: Prajwal Nautiyal
Last Update: 8 November 2022
A basic calculator program.
"""

from func import ent                # Importing the input function from func.py
import timeit as ti                 # Importing the timeit module to calculate the runtime of the program

def main():
    start = ti.default_timer()                                                                  # Starting the timer for the program
    try:                                                                    # Try block to catch the KeyboardInterrupt
        while True:                                                         # Infinite loop
            num = inp()                                                     # Calling the input function, stores the input in a tuple
            calT_start = ti.default_timer()                                 # Starting the timer for the calculation
            result = cal(num[0], num[1], num[2])                            # Calling the calculation function
            prnt(num[0], num[1], num[2], result)                            # Calling the output function
            calT_stop = ti.default_timer()                                  # Stopping the timer for the calculation
            print(f"Calculation Time: {calT_stop - calT_start} seconds")    # Printing the calculation time
    except KeyboardInterrupt:
        stop = ti.default_timer()                                                               # Stopping the timer for the program
        print(f"\n{'*'*20} Program Closed {'*'*20}\nTotal Runtime: {stop - start} seconds")     # Printing the total runtime of the program

def inp():
    a, b = ent()                    # Using the input function from func.py to take input of two numbers from the user
    ops = input("Choose one operation: ['+', '-', '*', '/'] ")              # Taking input of the operation to be performed
    return a, b, ops

def cal(num1:float, num2:float, op:str) -> float:                           # Defining the calculation function, type casting is used; takes two numbers and an operator as argument
    match op:                       # Using the match statement to match the operator
        case '+':
            val = num1 + num2
        case '-':
            val = num1 - num2
        case '*':
            val = num1 * num2
        case '/':
            val = num1 / num2
        case _:
            val = 0.0
    return val

def prnt(n1, n2, opr, valu):        # Defining the output function, takes the two inputs, the chosen operator and the result as argument
    print(f"The expression {n1}{opr}{n2} has result {valu}\nCtrl+C to Exit.")

if __name__ == "__main__":          # Source Control
    main()                          # Calling the main function