"""
Assignment No.: 1
Course: PROG12974
Name: Prajwal Nautiyal 
Sheridan Student Number: 991662442
Submission date: 29 September 2022
Instructor's name: Syed Tanbeer
Description: This is a program to calculate compound interest on a principal amount with values taken from user.
"""

# Taking all input values from the user
principal = int(input("Enter the principal amount:\t"))
interest_rate = int(input("Enter the rate of interest:\t"))
num_of_interest_compounded = int(input("Enter the number of times per year that the interest is compounded:\t"))
num_of_years = int(input("Enter the number of years the account will be left to earn interest:\t"))

# Converting the interest Percentage into Decimal Interest
decimal_Interest = interest_rate/100
# Calculating the final balance in the account after the inputted number of years
final_amount = principal*((1+(decimal_Interest/num_of_interest_compounded))**(num_of_years*num_of_interest_compounded))

# Printing the Output
print(f"\nPrincipal Amount:\t{principal}\
    \nAnnual Interest Rate:\t{interest_rate}%\
    \nNumber of times the Interest was compounded in one year:\t{num_of_interest_compounded}\
    \nNumber of Years the account earned Interest:\t{num_of_years}\
    \nThe Final Balance in the account:\t{final_amount:.2f}\nCompound interest calculator by: Prajwal Nautiyal, 991662442")