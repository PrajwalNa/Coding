"""
Dev: Prajwal Nautiyal
Last Update: 8 November 2022
A simple program to convert a date from dd/mm/yyyy format to dd monthname yyyy format.
"""

from time import sleep

__name__ = "__dateconv__"                   # Defining the main function

def dateconv():                             # Main Function
    try:
        while True:                         # Looping the program infinitely
            userin = datein()               # Calling the input function
            TorF = validate(userin)         # Validating the input
            conv = assign(userin)           # Converting the Date, saving it in a tuple
            printout(TorF, conv[0], conv[1], conv[2])
    except KeyboardInterrupt:               # Handling the Ctrl+C; keyboard interrupt
        print(f"\n{'*'*20}Program Closed{'*'*20}")

def datein():                               # User Input function to given instructions to the user on the format of input
    try:
        usr = input("Enter a date[dd/mm/yyyy]: ")
        daymonyr = usr.split("/")           # Splitting the input into a list
        return daymonyr                     # Returning the list
    except IndexError:
        print("!!Invalid Entry!!\nCtrl+C To Exit.")
        return ['00', '00', '0000']         # Returning a list with invalid value

def name(month):                            # Function to convert the month number into month name
    match month:
        case '01' : month = 'January'
        case '02' : month = 'February'
        case '03' : month = 'March'
        case '04' : month = 'April'
        case '05' : month = 'May'
        case '06' : month = 'June'
        case '07' : month = 'July'
        case '08' : month = 'August'
        case '09' : month = 'September'
        case '10' : month = 'October'
        case '11' : month = 'November'
        case '12' : month = 'December'
        case _: month = 'Invalid Month!!'
    return month

def validate(dmy):                          # Validating the Input, took the list as argument
    mnth = name(dmy[1])                     # Assigning the month name to a variable
    # Checking if the month is in the list of months with 31 days
    if mnth in  ['January', 'March', 'May', 'July', 'August', 'October', 'December']:
        if int(dmy[0]) in range(1,32):      # Checking if the date is valid or not for the respective months
            return True
        else:
            return False
    elif mnth == 'February':                # Checking if the month is February
        if int(dmy[2])%4 == 0:              # Checking if the year is a leap year
            if int(dmy[0]) in range(1,30):  # Checking if the date is valid or not for a leap year february
                return True
            else:
                return False
        else:
            if int(dmy[0]) in range(1,29):  # Checking if the date is valid or not for a non-leap year february
                return True
            else:
                return False
    # Checking if the month is in the list of months with 30 days
    elif mnth in ['April', 'June', 'September', 'November']:
        if int(dmy[0]) in range(1,31):      # Checking if the date is valid or not for the respective months
            return True
        else:
            return False
    else:                                   # If the month is not in either of the list of months
        return False
                

def assign(dmyr):                           # Converting the date into a different format
    # Assigning values of date month and year into respectuve variables
    date = dmyr[0]
    month = name(dmyr[1])
    year = dmyr[2]
    return date, month, year

def printout(vld, d, m, y):                 # Output Function, takes the validation flag, date, month and year as arguments
    if vld == True:                         # Checking if the date is valid or not with the help of the validation flag
        print("Date: "+d+"\nMonth: "+m+"\nYear: "+y+"\nCtrl+C To Exit.")
        sleep(2.0)                          # Waiting for 2 seconds before restarting the program
    else:
        print("!!Invalid Entry!!\nCtrl+C To Exit.")
        sleep(2.0)

if __name__ == "__dateconv__":              # Source Control
    dateconv()                              # Calling the main function