"""
Developer: Prajwal Nautiyal
Last Update: 3 November 2022
Just a random program I made while bored in class. Enjoy!
"""

import random
import re

def main():
    try:                                                # Try-Except block to handle keyboard interrupt
        log = {}                                        # Dictionary to log the entries for one session
        while True:
            n1, n2 = getin()                            # Function call to get the input from the user
            if n1+' '+n2 and n2+' '+n1 not in log:      # Checking if the user input is in the log
                prcnt = calcLove()                      # Function call to calculate the love percentage
                lg = giveout(n1, n2, prcnt)
                log.update({n1+' '+n2 : lg})
            elif n2+' '+n1 in log:                      # Checking if the input is in reversed order
                print(log.get(n2+' '+n1),'\n')
            else:                                       # Printing the log entry
                print(log.get(n1+' '+n2),'\n')
    except KeyboardInterrupt:
        print(f"\n{'*'*20}Program Closed{'*'*20}")

def getin():                                            # Function to get the input from the user
    name1 = input("Enter first person's name: ")
    name2 = input("Enter second person's name: ")
    return name1, name2

def calcLove():
    bs_prcnt = random.uniform(0.0, 100.0)               # Using random module to generate a random number between 0.0 and 100.0
    return bs_prcnt

def giveout(p1 : str, p2 : str, percnt : float):
    if re.match('^[A-Za-z]\w+', p1 and p2):             # Using regex to check if the input is a valid name,well honestly it just checks if the input is a string of alphabets
        if percnt >= 80.00:                             # If the random number generated is greater than or equal to 80.00
            out = f"Love % between {p1} & {p2} is {percnt:.2f}%\n...Soulmates? Nahh go back to your Disney Movie."
        elif percnt >= 60.00 and percnt < 80.00:        # If the random number generated is greater than or equal to 60.00 and less than 80.00
            out = f"Love % between {p1} & {p2} is {percnt:.2f}%\nYou have it great don't ya? God damn love birds."
        elif percnt >= 40.00 and percnt < 60.00:        # If the random number generated is greater than or equal to 40.00 and less than 60.00
            out = f"Love % between {p1} & {p2} is {percnt:.2f}%\nIt'll be hard, but you probably wouldn't be."
        elif percnt >= 20.00 and percnt < 40.00:        # If the random number generated is greater than or equal to 20.00 and less than 40.00
            out = f"Love % between {p1} & {p2} is {percnt:.2f}%\nYou're better off without each other, unless you're in t for money or a green card,then tolerate a little bit more."
        else:                                           # If the random number generated is less than 20.00
            out = f"Love % between {p1} & {p2} is {percnt:.2f}%\nThis is not love bro, one of you has kept the other hostage in their basement. And stop hopin that Stockholm Syndrone is gonna fix it all."
        print(f"{out}\nCtrl+C To Exit.\n")
    else:                                               # If the input is not a string of alphabets
        out = 'Null'
        print("Invalid Input!!")
    return out

if __name__ == "__main__":
    main()