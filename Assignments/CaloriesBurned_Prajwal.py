"""
Assignment No.: 1
Course: PROG12974
Name: Prajwal Nautiyal 
Sheridan Student Number: 991662442
Submission date: 29 September 2022
Instructor's name: Syed Tanbeer
Description: This program calculates how many calories a person burns during an exercise activity, 
by taking input for gender, age, weight, heart rate and duration of exercise activity from the user.
"""
# Taking unput from user
gender = input("Enter your gender[M/F]: ")
age = int(input("Enter your age: "))
weight = int(input("Enter your weight(in lbs): "))
heart_rate = int(input("Enter your heart rate while exercising(in bpm): "))
excercise_duration = int(input("Enter the duration of the exercise session(in mins): "))

# Checking which formula to use for calculation of Calories burned or if user input was wrong, to present the user with an error
if gender == "M":
    Calories_Burned = ((age*0.2017)-(weight*0.09036)+(heart_rate*0.6309)-55.0969)*(excercise_duration/4.184)
    output = f"\nEnter your gender (M = Male, F = Female):\t{gender}\
        \nEnter your age:\t{age} years\
        \nEnter your weight (lbs):\t{weight}\
        \nEnter your heart rate (bpm):\t{heart_rate}\
        \nEnter the duration of exercise (in mins):\t{heart_rate}\
        \nYou burned {Calories_Burned:.2f} calories."
elif gender == "F":
    Calories_Burned = ((age*0.074)-(weight*0.05741)+(heart_rate*0.4472)-20.4022)*(excercise_duration/4.184)
    output = f"\nEnter your gender (M = Male, F = Female):\t{gender}\
        \nEnter your age:\t{age} years\
        \nEnter your weight (lbs):\t{weight}\
        \nEnter your heart rate (bpm):\t{heart_rate}\
        \nEnter the duration of exercise (in mins):\t{heart_rate}\
        \nYou burned {Calories_Burned:.2f} calories."
else:
    output = "!!Invalid Input!!\nPlease choose either of the genders and enter as specified in the square brackets"

# Printing the output to the user
print(output+"\nCalories Burned calculator by: Prajwal Nautiyal, 991662442")