"""
Dev: Prajwal Nautiyal
Last Update: 8 November 2022
A function to test modularisation in python, 
it calculates the average of two numbers and the sum of numbers from first number to the second number.
"""

import func         # module call to use function from another module

def avgmain():      # main function
    try:            # try block
        while True:
            a1, a2 = func.ent()                         # function call to get the input from the user
            outp = calavg(a1, a2)                       # function call to calculate the average, stores the average in a tuple
            num = func.sumfromAtoB(a1,a2)               # function call to calculate the sum of the range numbers from a1 to a2, stores the sum in a tuple
            func.out(num[0], num[1], num[2])            # calling the function from another module print the sum of the numbers in range from a1 to a2
            output(a1, a2, outp)                        # calling the function to print the mean
    except KeyboardInterrupt:                           # except block to handle keyboard interrupt
        print(f"\n{'*'*20}Prgram Closing{'*'*20}")

def calavg(n1, n2):                                     # function to calculate the average
    cal = (n1 + n2) / 2
    return cal

def output(uin1, uin2, num):                            # function to print the average, takes both the inputs and the average as argument
    print(f"The mean of {uin1} and {uin2} is {num}")    # using python's f-string to print the output
    print("Ctrl^C to Exit.")

avgmain()                                               # calling the main function
