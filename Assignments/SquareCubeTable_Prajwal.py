"""
Assignment No.: 1
Course: PROG12974
Name: Prajwal Nautiyal 
Sheridan Student Number: 991662442
Submission date: 29 September 2022
Instructor's name: Syed Tanbeer
Description: The program displays a table of squares and cubes of numbers from 1 to 5,
if the input is less than or equal to 5,if the input is greater then the program is terminated.
"""

# Taking Input from User
user_input = int(input("Enter a number between 1 and 10:"))

# Declaring Constants for Calculations
num1 = 1; num2 = 2; num3 = 3; num4 = 4; num5 = 5

#Calculating the Table and storing it into a Variable
Output_Table = f"N\tN^2\tN^3\
    \n{num1}\t{num1**2}\t{num1**3}\
    \n{num2}\t{num2**2}\t{num2**3}\
    \n{num3}\t{num2**2}\t{num3**3}\
    \n{num4}\t{num4**2}\t{num4**3}\
    \n{num5}\t{num5**2}\t{num5**3}\nSquare-Cube Table by: Prajwal Nautiyal, 991662442"

# Checking if the user input is greater than five.
if user_input > 5:
    Output = "Input is greater than 5. Goodbye\nSquare-Cube Table by: Prajwal Nautiyal, 991662442"
else:
    Output = Output_Table

# Printing the Output to the user, and printing a line for making the output stand out
print(Output+"\n"+'-'*40)