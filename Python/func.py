"""
Dev: Prajwal Nautiyal
Last Update: 8 November 2022
On its own this program calculates the sum from first number to the second number, 
but mostly I just used the functions defined here in other programs.
"""

def main():                                         # The main function to call all functions
    try:
        while True:
            usrin1, usrin2 = ent()                  # Calling the input function
            num = sumfromAtoB(usrin1, usrin2)       # Calling the function to calculate the sum of the numbers in range from usrin1 to usrin2, stores the sum in a tuple
            out(num[0], num[1], num[2])             # Calling the function to print the sum of the numbers in range from usrin1 to usrin2
    except KeyboardInterrupt:
        print(f"\n{'*'*20}Program Closing{'*'*20}")

def ent():                                          # Taking input from the user
    flr = float(input("Enter first Number: "))
    ceil = float(input("Enter second Number: "))
    return flr, ceil                                # Returning the input

def sumfromAtoB(floor, ceiling):                    # Calculating for the output
    add = 0
    for c in range(floor, ceiling+1):               # range function takes the floor and ceiling as argument, ceiling+1 is used to include the ceiling number in the range
        add += c                                    # adding the numbers in the range
    return floor, ceiling, add                      # Returning the values

def out(n1, n2, n3):                                # Output function
    print(f"\nThe sum from {n1} to {n2} is {n3}")   # Using python's f-string to print the output
    print("Ctrl^C to Exit")

if __name__ == "__main__":                          # Source Control
    main()                                          # Calling the main function