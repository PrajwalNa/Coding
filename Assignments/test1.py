"""
Quiz/Lab: 2
Name: Prajwal Nautiyal
Set: A
Submission Date: 11 October 2022
Instructor's Name: Syed Tanbeer
"""

i = 1# Loop variable
counter = 2# Counter for total number of words

# Counters for individual words below
word_counter1 = 0
word_counter2 = 0
word_counter3 = 0
word_counter4 = 1
word_counter5 = 0

output = ""# Defining the output variable
while i != 0:
    user_input = input("Enter a word (enter a '.' to terminate): ")
    if user_input != '.':# Checking for terminating input and filling the respective counters
        output = output + " " + user_input
        counter = counter + 1
        if len(user_input) == 1:
            word_counter1 = word_counter1 + 1
        elif len(user_input) == 2:
            word_counter2 = word_counter2 + 1
        elif len(user_input) == 3:
            word_counter3 = word_counter3 + 1
        elif len(user_input) == 4:
            word_counter4 = word_counter4 + 1
        elif len(user_input) == 5:
            word_counter5 = word_counter5 + 1
    else:
        i = 0
        output = output + user_input

print(f"Prajwal says, \"{output}\"\
    \nTotal word count in the sentence: {counter}\
    \nOne Letter word count: {word_counter1}\
    \nTwo Letter word count: {word_counter2}\
    \nThree Letter word count: {word_counter3}\
    \nFour Letter word count: {word_counter4}\
    \nFive Letter word count: {word_counter5}")# Printing the output