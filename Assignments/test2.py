"""
Quiz/Lab: 2
Name: Prajwal Nautiyal
Sheridan Student ID: 991662442
Set: A
Submission Date: 11 October 2022
Instructor's Name: Syed Tanbeer
"""

# Taking input
date = input("Enter a date (as Month DD, YYYY): ")
# Spilitting the year from date and month
dateList = date.split(',')
year = dateList[1]
daymon = dateList[0]# Saving the day and month together
datelist2 = daymon.split(' ')# Splitting day and month
month = datelist2[0]
day = datelist2[1]

i = 0# Cpunter variable
month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
while i < 12:# while loop to check for the month assignment
    if month in month_list[i]:
        month = str(i + 1)# Since i is the index of the list and list starts at 0
    i = i + 1

print(f"Date is converted format: {year}/{month}/{day}")