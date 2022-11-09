"""
Dev: Prajwal Nautiyal
Last Update: 8 November 2022
Program to print a triangle and a quadrilateral.
"""

row = int(input("Enter number of rows: "))                              # Taking input of the number of rows from the user
colum = int(input("Enter number of columns: "))                         # Taking input of the number of columns from the user

for i in range(row):                                                    # Loop to print the the top half of the triangle
    for j in range(i+1):                                                # Loop to print the number of stars in each row
        if j == 0 or j == i:                                            # If statement to print the first and last column of the triangle
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()                                                             # Passing control to the next line

for k in range(row-2,-1,-1):                                            # Loop to print the bottom half of the triangle, row -2 is used so that the cone of the triangle well defined
    for l in range(k,0,-1):                                             # Loop to print the number of stars in each row
        if l == 0 or l == k:                                            # If statement to print the first and last column of the triangle
            print('*', end=" ")
        else:
            print(" ", end=" ")
    print('*')

print("\n"+"="*50+"\n")                                                 # Printing a line to separate the triangle and the quadrilateral

for a in range(row):                                                    # Loop to print the top half of the quadrilateral
    for b in range(colum):                                              # Loop to print the number of stars in each row
        if (a == 0 or a == row - 1 or b == 0 or b == colum - 1):        # If statement to print the first and last column of the quadrilateral
            print('*', end = '  ')#
        else:
            print(' ', end = '  ')
    print()                                                             # Passing control to the next line