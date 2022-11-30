"""
Assignment No.: 2
Course: PROG12974
Name: Prajwal Nautiyal
Submission date: 16 November 2022
Instructor's name: Syed Tanbeer
Menu Based Program for carrying out various functions
Most print functions in this program are using octal notation for ANSI escape sequences to Colourise the output, so the '\033['
"""

import re                               # Importing regex module
import sys                              # Importing sys module to use the exit function
import function_tools as ft             # Importing the function_tools module as ft to use the functions defined in it
from time import sleep                  # Importing sleep function from time module to use in the exit process


def main():                             # Main function
    try:
        while True:                     # While loop to keep the program running, no exit condition because that is carried out in the routing finction
            usr_choice = getinput()     # Calling the input function to get the user choice from the menu
            functioncall(usr_choice)    # Calling the routing function to direct the program to the the user's preference from the menu
    except KeyboardInterrupt:           # Exception handling for keyboard interrupt
        print(f"\n\033[1;92m{'-'*20}Program Closing{'-'*20}\033[22;00m")

def functioncall(user):                 # Routing function
    match user:                         # Matching the user input with the menu options
        case '1':
            DrawShape()                 # Calling the DrawShape function if user chose the first option
        case '2':
            isFermat()                  # Calling the Fermat function if user chose the second option
        case '3':
            try:
                n = int(input("Enter the value for n: "))   # Getting the value of n from the user to feed into the factorial power series function
                fc = facto_power_series(n)                  # Calling the factorial power series function and storing the result in a variable
                output(fc)                                  # Displaying the result of the factorial power series function
            except ValueError:          # Exception handling for incorrect input
                print("\n\033[1;91mError: Invalid Input!! Please enter a positive integer\033[22;00m")
            except RecursionError:      # Exception handling for recursion error
                print("\n\033[1;91mError: Recursion limit exceeded!! Please only enter small positive integer values\033[22;00m")
        case '4':
            check_password()            # Calling the check password function if user chose the fourth option
        case '5':
            temp = ""
            for c in "Thank you for using my menu program!":
                temp += c
                print(f"\033[1;92m\r{temp}",end="")         # Using carriage return to print the exit message one character at a time
                sleep(0.04)
            print("\033[22;00m")
            sys.exit()                  # Exiting the program using the in-built exit function if user chose the fifth option
        case _:                         # Default case if user enters an invalid input
            print("\033[1;91mInvalid choice\033[22;00m")

def getinput():                         # Function to present the user with a menu and their input choice
    print(f"\n\033[1;96m{'*'*20} Menu {'*'*20}")
    usr_choice = input("1 - Draw a Shape\n2 - Fermat's Last Theorem\n3 - Facto-Power Series\n4 - Check Password\n5 - Quit\033[22;00m\nEnter your choice: ")
    return usr_choice

def DrawShape():                        # Function to draw a shape based on the user's input
    print()                             # To print a blank line for aesthetic reasons
    # Getting the user's choice to draw a triangle or a rectangle
    choice = input("\033[1;96ma - Draw a triangle\nb - Draw a rectangle\033[22;00m\nEnter your choice: ")
    match choice.lower():               # Matching the user's choice
        case 'a':                       # If user chose to draw a triangle
            try:
                row = int(input("Enter the side of triangle: "))                            # Getting the side of the triangle from the user
                print()                 # To print a blank line for aesthetic reasons
                for i in range(row):
                    for j in range(i+1):
                        if (j == 0 or j == i or i == row-1):                                # Checking if the current position is the first or last position of the row or the last row
                            print("\033[1;92m*\033[22;00m",end=" ")
                        else:
                            print(" ",end=" ")
                    print()             # Printing a new line to pass control to the next row
            except ValueError:          # Exception handling for incorrect input
                print("\n\033[1;91mError: Invalid Input!! Please enter a positive integer\033[22;00m")
        case 'b':                       # If user chose to draw a rectangle
            # Getting the length and width of the rectangle from the user
            try:
                row = int(input("Enter the length: "))
                colum = int(input("Enter the width: "))
                print()                 # To print a blank line for aesthetic reasons
                for a in range(row):
                    for b in range(colum):
                        if (a == 0 or a == row - 1 or b == 0 or b == colum - 1):            # Checking if the current position is the first or last position of the row or the last row
                            print("\033[1;92m*\033[22;00m", end = " ")
                        else:
                            print(" ", end = " ")
                    print()             # Printing a new line to pass control to the next row
            except ValueError:          # Exception handling for incorrect input
                print("\n\033[91mError: Invalid Input!! Please enter a positive integer\033[00m")
        case _:                         # Default case if user enters an invalid input
            print("\033[1;91mInvalid choice\033[22;00m")
    
def isFermat():                         # Function to check if Fermat's last theorem is true or not
    try:
        # Getting the values of a , b, c and n - the power from the user
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        c = int(input("Enter c: "))
        n = int(input("Enter n: "))
        if a<=0 or b<=0 or c<=0 or n<=0:                    # Checking if any of the values are less than or equal to zero
            print("\033[1;91mPlease enter positive values only!\033[22;00m")
        else:    
            if n > 2 and ft.power(a,n) + ft.power(b,n) != ft.power(c,n):                    # Using the power function from the function_tools.py file to check if the theorem is true or not
                print(f"\n\033[1;92mFor n = {n}, Left hand side != Right hand side: The theorem holds.\033[22;00m")
            elif n <= 2 and ft.power(a,n) + ft.power(b,n) != ft.power(c,n):
                print(f"\n\033[1;92mFor n = {n}, Left hand side != Right hand side: The theorem holds.\033[22;00m")
            else:
                print(f"\n\033[1;92mFor n = {n}, Left hand side = Right hand side: The theorem holds.\033[22;00m")
    except ValueError:                  # Exception handling for incorrect input
        print("\n\033[1;91mError: Invalid Input!! Please enter a positive integer\033[22;00m")
    except RecursionError:              # Exception handling for recursion error
        print("\n\033[1;91mError: Recursion limit exceeded!! Please only enter small positive integer values (<995) for n\033[22;00m")  

def facto_power_series(n : float) -> float:                 # Function to calculate the factorial power series
    series_sum = ft.series(n)           # Using the series function from the function_tools.py file to calculate the factorial power series
    return series_sum                   # returing the sum of the factorial power series

def output(fact : float):               # Output function for factorial power series
    print(f"\n\033[1;92mThe sum of your series is: {fact}\033[22;00m")

def check_password():                   # Function to check if the password entered by the user is valid or not
    password = input("Enter password: ")                    # Getting the password from the user
    if len(password) < 8:               # Checking if the password is less than 8 characters and setting a boolean variable to false if it is
        len_check = False
    else:
        len_check = True
    # Using regex to check if the password follows the set rules
    if re.search("[a-z]",password) is not None:             # Checking if the password has a lowercase letter
        lower_check = True
    else:  
        lower_check = False
    if re.search("[A-Z]",password) is not None:             # Checking if the password has an uppercase letter
        upper_check = True
    else:
        upper_check = False
    if re.search("[0-9]",password) is not None:             # Checking if the password has a digit
        num_check = True
    else:
        num_check = False
    if re.search("[!@#$%^&*?-_+=]",password) is not None:   # Checking if the password has a special character
        special_check = True
    else:
        special_check = False
    if re.search("[<>]",password) is not None:              # Checking if the password has a < or > character
        rule_check = False
    else:
        rule_check = True
    # Checking if all the flags are true and displaying the result if they are
    if len_check and lower_check and upper_check and num_check and special_check and rule_check:
        print("\n\033[1;92mValid password\033[22;00m")
    if not len_check:                   # if the password is less than 8 characters, printing the appropriate error message
        print("\n\033[1;91mInvalid Password!! Password must be at least 8 characters long\033[22;00m")
    if not lower_check:                 # if the password does not have a lowercase letter, printing the appropriate error message
        print("\n\033[1;91mInvalid Password!! Password must contain at least one lowercase letter\033[22;00m")
    if not upper_check:                 # if the password does not have an uppercase letter, printing the appropriate error message
        print("\n\033[1;91mInvalid password!! Password must contain at least one uppercase letter\033[22;00m")
    if not num_check:                   # if the password does not have a digit, printing the appropriate error message
        print("\n\033[1;91mInvalid password!! Password must contain at least one number\033[22;00m")
    if not special_check:               # if the password does not have a special character, printing the appropriate error message
        print("\n\033[1;91mInvalid password!! Password must contain at least one special character, excluding '<' and '>'\033[22;00m")
    if not rule_check:                  # if the password has a < or > character, printing the appropriate error message
        print("\n\033[1;91mInvalid password!! Password must not contain '<' or '>'\033[22;00m")

if __name__ == "__main__":              # Source Control
    main()                              # Calling the main function
