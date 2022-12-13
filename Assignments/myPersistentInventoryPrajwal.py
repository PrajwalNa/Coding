"""
Assignment No.: 4
Course: PROG12974
Name: Prajwal Nautiyal
Submission date:
Instructor's name: Syed Tanbeer
------------------------------------------------------------------------------------------------------------------------
This program is a persistent inventory system that allows the user to perform various operations on the inventory database.
It uses a text file to store the inventory data and performs the operations on the file.
The code checks for the existence of the file and creates it if it doesn't exist.
Similarl operations to the the previous assignment are performed on the file, but the file is not read into a dictionary.
------------------------------------------------------------------------------------------------------------------------
ANSI codes used for colored output: 
033[91m - Red
033[92m - Green
033[93m - Yellow
033[94m - Blue
033[96m - Cyan
"""


from datetime import datetime           # Importing the datetime module to get the current date and time
import re                               # Importing the regular expression module to check if the item code is valid
import sys                              # Importing the sys module to exit the program
import time                             # Importing the time module to use the sleep function
from os.path import exists              # Importing the exists function from the os.path module to check if the file exists

# Main Function
def main():
    log_check()                         # Check if the log file exists
    try:
        while True:
            menu()
            choice = getinput()
            Route(choice)
    except KeyboardInterrupt:
        print(f"\n\033[92m{'*'*30} Program Closed {'*'*30}\033[0m")

# Printing the Menu
def menu():
    print(f"\n\033[93m{'+'*30} Inventory Database Operations {'+'*30}")
    print("""
            1. Display all items
            2. Look up an item in the Inventory
            3. Add a new item to the Inventory
            4. Update an item in the Inventory
            5. Delete an item from the Inventory
            6. Find items by Category
            7. Item Count and Average price by Category
            8. Most Expensive Item by Category
            9. Total Price of each item in the Inventory
            10. Exit\033[0m
        """)

# Get input from the user        
def getinput():
    try:
        choice = int(input("\nEnter your choice: "))
        return choice
    except ValueError:                  # If the user enters a non-integer value
        print("\033[91mPlease enter a number!!\033[0m")
        return getinput()               # Call the function again to get the input

# Routing function to direct the user to their desired choice    
def Route(choice : int):
    match choice:
        case 1:                         # Display all items
            op1()
        case 2:                         # Look up an item in the Inventory
            op2()
        case 3:                         # Add a new item to the Inventory
            op3()
        case 4:                         # Update an item in the Inventory
            op4()
        case 5:                         # Delete an item from the Inventory
            op5()
        case 6:                         # Find items by Category
            op6()
        case 7:                         # Item Count and Average price by Category
            op7()
        case 8:                         # Most Expensive Item by Category
            op8()
        case 9:                         # Total Price of each item in the Inventory
            op9()
        case 10:                        # Exit, using a carriage return to print the exit message one character per 0.02 seconds
            temp = ""
            for c in "Thank you for using the Inventory Database System":
                temp += c
                print(f"\033[92m\r{temp}",end="")
                time.sleep(0.02)
            print("\033[0m")
            sys.exit()                  # Exit call from the sys module
        case _:                         # If the user enters a choice other than the ones mentioned above
            print("\033[91mPlease enter a valid option!!\033[0m")
            # Using recursion to call the function again to get the input in case of an invalid choice, instead of using a loop
            choice = getinput()
            Route(choice)

# Option 1: Display all items           
def op1():
    try:
        print(f"\n\033[96m{'*'*30} Displaying all items {'*'*30}")
        # Printing the header
        print(f"{'Item Code':<15}{'Item Name':<15}{'Category':<15}{'Price (CA$)':<15}{'Quantity':<15}")  
        print(f"{'-'*75}")              # Printing the header separator
        with open('inventory_Prajwal.txt','r') as f:
            # Printing the contents of the file
            print(f.read().lstrip(f"{'Item Code':<15}{'Item Name':<15}{'Category':<15}{'Price':<15}{'Quantity':<15}\n"))
    except FileNotFoundError:
        print("\033[91mError: No File to Read!!\033[0m")
        sys.exit("\033[93mExiting the program\033[0m")

# Option 2: Look up an item in the Inventory
def op2():
    print(f"\n\033[96m{'*'*30} Look up an item in the Inventory {'*'*30}\033[0m")
    itemcode = input("Enter the item code: ").upper()
    # Convert the item code to uppercase to match the dictionary keys
    if checkItem(itemcode):             # Check if the item code exists in the dictionary
        # Printing the header
        print(f"\033[96m{'Item Code':<15}{'Item Name':<15}{'Category':<15}{'Price (CA$)':<15}{'Quantity':<15}")
        print(f"{'-'*75}")              # Printing the header separator
        lineList = readFile('inventory_Prajwal.txt')                        # Read the file and store the contents in a list
        for line in lineList:
            if itemcode in line:
                print(line)
    else:                               # If the item code does not exist in the dictionary
        print("\033[91mItem not found\033[0m")

# Option 3: Add a new item to the Inventory
def op3():
    print(f"\n\033[96m{'*'*30} Add a new item to the Inventory {'*'*30}\033[0m")
    itemcode = input("Enter the item code: ").upper()                       # Convert the item code to uppercase to match the dictionary keys
    # Check if the item code is in the correct format using regex
    if checkItem(itemcode):             # Check if the item code exists in the file
        print("\033[94mItem already exists\033[0m")
    else:                               # If the item code does not exist in the dictionary
        try:
            itemname = input("Enter the item name: ").capitalize()          # Capitalising the first letter of itemname to match the dictionary format
            while itemname == "":       # Loop to make sure itemname is not empty
                print("\033[91mItem name cannot be empty\033[0m")
                itemname = input("Enter the item name: ").capitalize()
            category = input("Enter the item category: ").capitalize()      # Capitalising the first letter of category to match the dictionary format
            # Checking if the category is invalid, else add the item to the dictionary
            while not validate(category):
                print("\033[91mInvalid category\033[0m")
                print("\033[94mValid categories are: Fruit, Vegetable, Dairy\033[0m")
                category = input("Enter the item category: ").capitalize()      
            else:
                # Checking if the category does not match the itemcode, else add the item in the dictionary
                if match(itemcode, category):
                    price = float(input("Enter the item price: "))
                    quantity = int(input("Enter the item quantity: "))
                    # Adding the item to the file
                    writeFile("inventory_Prajwal.txt" ,"A", data=[itemcode, itemname, category, price, quantity])
                    print("\033[92mItem added successfully\033[0m")
        except ValueError:              # If the user enters a non-integer value for quantity or a non-float value for price
            print("\033[91mIllegal value entered!!\033[0m")

# Option 4: Update an item in the Inventory
def op4():
    print(f"\n\033[96m{'*'*30} Update an item in the Inventory {'*'*30}\033[0m")
    itemcode = input("Enter the item code: ").upper()
    # Convert the item code to uppercase to match the values in the file
    if not checkItem(itemcode):         # Check if the item code to be updated exists in the dictionary
        print("\033[91mItem not found\033[0m")
    else:
        print("\033[94mIf you don't want to change a value just leave the input empty\
            \nIncase of Price and Quantity enter 0.0 and -ve values respectively\033[0m")
        value = unpackFile()            # Get the list of items from the file
        val = [i for i in value if i[0] == itemcode]
        try:                            # Try to update the item
            itemname = input("Enter the name: ").capitalize()
            if itemname == "":          # If the user does not want to change the name
                itemname = val[0][1]    # Set the name to the current name
            # Capitalising the first letter of category to match the dictionary format
            category = input("Enter the category: ").capitalize()               
            if category == "":          # If the user does not want to change the category
                category = val[0][2]    # Set the category to the current category
            # Check if the category is valid
            while not validate(category):
                print("\033[91mInvalid category\033[0m")
                print("\033[94mValid categories are: Fruit, Vegetable, Dairy\033[0m")
                category = input("Enter the item category: ").capitalize()   
            else:
                # Checking if the category does not match the itemcode, else update the item
                if match(itemcode, category):
                    price = float(input("Enter the price: "))
                    if price == 0.0:    # If the user does not want to change the price
                        price = val[0][3]       # Set the price to the current price
                    quantity = int(input("Enter the quantity: "))
                    if quantity < 0:    # If the user does not want to change the quantity
                        quantity = val[0][4]    # Set the quantity to the current quantity
                    # Call the function to write the data to the file
                    writeFile("inventory_Prajwal.txt" ,'U', data=[itemcode, itemname, category, price, quantity])  
        except ValueError:              # If the user enters a non-integer value for quantity or a non-float value for price
            print("\033[91mIllegal value entered!!\033[0m")

# Option 5: Delete an item from the Inventory
def op5():
    print(f"\n\033[96m{'*'*30} Delete an item from the Inventory {'*'*30}\033[0m")
    itemcode = input("Enter the item code: ").upper()                       # Convert the item code to uppercase to match the item code in the file
    # Check if the item code to be deleted exists in the list, else print the error message
    if checkItem(itemcode):
        writeFile("inventory_Prajwal.txt" ,'D', itemcode)
    else:
        print("\033[91mItem not found\033[0m")

# Option 6: Find items by Category
def op6():
    print(f"\n\033[96m{'*'*30} Find items by Category {'*'*30}\033[0m")
    category = input("Enter the category: ").capitalize()                   # Capitalising the first letter of category to match the dictionary format
    # Checking if the category is valid, else print error message
    if validate(category):
        # Printing the header
        print(f"\033[96m{'Item Code':<15}{'Item Name':<15}{'Price (CA$)':<15}{'Quantity':<15}")
        print(f"{'-'*60}")              # Print the header separator
        lines = unpackFile()            # Get the list of items from the file
        for line in lines:              # Loop through the list of items
            # Checking if the category matches the category entered by the user
            if line[2] == category:
                print(f"{line[0]:<15}{line[1]:<15}{line[3]:<15}{line[4]:<15}")
        print("\033[0m")
    else:
        print("\033[91mPlease enter a valid category!!\033[0m")

# Option 7: Printing Item Count and Average Price of each Category
def op7():
    fruitcount = 0                      # Initialize the fruit count to 0
    fruitprice = 0.0                    # Initialize the fruit price to 0
    dairycount = 0                      # Initialize the dairy count to 0
    dairyprice = 0.0                    # Initialize the dairy price to 0
    vegcount = 0                        # Initialize the vegetable count to 0
    vegprice = 0.0                      # Initialize the vegetable price to 0
    lines = unpackFile()                # Get the list of items from the file
    for key in lines:                   # Loop through the dictionary and calculate the item count and total price of items in each category
        # If the category is Fruit, increment the fruit count and add the price to the fruit price
        if key[2] == "Fruit":
            fruitcount += 1
            fruitprice += key[3]
        # If the category is Dairy, increment the dairy count and add the price to the dairy price
        elif key[2] == "Dairy":
            dairycount += 1
            dairyprice += key[3]
        # If the category is Vegetable, increment the vegetable count and add the price to the vegetable price
        elif key[2] == "Vegetable":
            vegcount += 1
            vegprice += key[3]
    # Calculating the average price of each category
    avgfruitprice = fruitprice / fruitcount
    avgdairyprice = dairyprice / dairycount
    avgvegprice = vegprice / vegcount
    print(f"\n\033[96m{'*'*30} Printing Item Count and Average Price of each Category {'*'*30}")
    # Printing the header
    print(f"{'Category':<15}{'Item Count':<15}{'Average Price (CA$)':<20}")
    print(f"{'-'*50}")                  # Print the header separator
    # Printing the item count and average price of each category in a tabular format
    print(f"{'Fruit':<15}{fruitcount:<15}{avgfruitprice:<20}\
            \n{'Dairy':<15}{dairycount:<15}{avgdairyprice:<20}\
            \n{'Vegetable':<15}{vegcount:<15}{avgvegprice:<20}\033[0m")

# Option 8: Most Expensive Item for each Category
def op8():
    maxFruit = 0.0                      # Initialize the maximum fruit price to 0
    maxDairy = 0.0                      # Initialize the maximum dairy price to 0
    maxVeg = 0.0                        # Initialize the maximum vegetable price to 0
    FruitID = ""                        # Initialize the fruit item code to an empty string
    DairyID = ""                        # Initialize the dairy item code to an empty string
    VegID = ""                          # Initialize the vegetable item code to an empty string
    lines = unpackFile()                # Get the list of items from the file
    count = 0
    print(f"\n\033[96mMost Expensive Item for each Category\033[0m")
    for item in lines:                  # Loop through the list and find the maximum price of each category
        print(f"\033[92m\r{' > '*count}", end=" ")      # Print the progress bar
        count += 1
        time.sleep(0.2)                 # Sleep for 0.2 seconds
        # If the category is Fruit and the price is greater than the maximum fruit price, update the maximum fruit price and fruit item code
        if item[2] == "Fruit":
            if item[3] > maxFruit:
                maxFruit = item[3]
                FruitID = [item[1], item[2], item[3], '', '']
        # If the category is Dairy and the price is greater than the maximum dairy price, update the maximum dairy price and dairy item code
        elif item[2] == "Dairy":
            if item[3] > maxDairy:
                maxDairy = item[3]
                DairyID = [item[1], item[2], item[3], '', '']
        # If the category is Vegetable and the price is greater than the maximum vegetable price, update the maximum vegetable price and vegetable item code
        elif item[2] == "Vegetable":
            if item[3] > maxVeg:
                maxVeg = item[3]
                VegID = [item[1], item[2], item[3], '', '\n']
    currentTime = datetime.now().ctime()                # Get the current time
    # Write the header to the file
    writeFile('expItem_Prajwal.txt', 'A', [currentTime, '\n', '\rMost Expensive Item (CA$)', '', '']) 
    writeFile('expItem_Prajwal.txt', 'A', FruitID)      # Write the values to the file
    writeFile('expItem_Prajwal.txt', 'A', DairyID)      # Write the values to the file
    writeFile('expItem_Prajwal.txt', 'A', VegID)        # Write the values to the file
    writeFile('expItem_Prajwal.txt', 'A', data=[f"{'-'*15}", f"{'-'*15}", f"{'-'*15}", f"{'-'*15}", f"{'-'*15}"])  
    print("\nFile Saved Sucessfully\033[0m")

# Option 9: Total Price of each item in the Inventory
def op9():
    print(f"\n\033[96mTotal Price of each item in the Inventory\033[0m")
    lines = unpackFile()                # Get the list of items from the file
    currentTime = datetime.now().ctime()                # Get the current time
    # Write the header to the file
    writeFile('total_Prajwal.txt', 'A', data=[currentTime, '\n', '\rName', 'Category', 'Total Price(CA$)']) 
    for count in range(10):
        print(f"\033[92m\r{' > '*count}", end=" ")      # Print the progress bar
        time.sleep(0.2)                 # Sleep for 0.2 seconds
    for key in lines:                   # Loop through the list and print the values (excluding category) in a tabular format
        # Write the values to the file
        writeFile('total_Prajwal.txt', 'A', data=[key[1], key[2], key[3] * key[4], '', ''])
    # Add a new line to the file to seperate the data
    writeFile('total_Prajwal.txt', 'A', data=[f"{'-'*15}", f"{'-'*15}", f"{'-'*15}", f"{'-'*15}", f"{'-'*15}"])  
    print("\nFile Saved Sucessfully\033[0m")

def checkItem(itemcode):
    if re.match(r"^(F|V|D){1}[0-9]{2,3}$", itemcode):
        lines = readFile("inventory_Prajwal.txt")       # Read the lines from the file
        for line in lines:              # Loop through the list of lines
            if line.startswith(itemcode):               # If the line starts with the item code, return True
                return True
        else:
            return False                # If the line does not start with the item code, return False
    else:                               # If the item code is not in the correct format
        print("\033[91mPlease enter a valid item code\033[0m")
        print("\033[91mItem code should be in the format [F/V/D][0-9][0-9][0-9]\033[0m")
        
# Function to validate the category
def validate(category):
    # If the category is not one of the three categories, return False
    if category not in ["Fruit", "Dairy", "Vegetable"]:
        return False
    # If the category is one of the three categories, return True
    else:
        return True

# Function to make sure the user entered a category coincinding with the item code
def match(itemcode, category):
    # Checking if the item code starts with F and the category is not Fruit
    if itemcode.startswith("F") and category != "Fruit":
        print("\033[91mItem code and category do not match!!\033[0m")
        return False
    # Checking if the item code starts with D and the category is not Dairy
    elif itemcode.startswith("D") and category != "Dairy":
        print("\033[91mItem code and category do not match!!\033[0m")
        return False
    # Checking if the item code starts with V and the category is not Vegetable
    elif itemcode.startswith("V") and category != "Vegetable":
        print("\033[91mItem code and category do not match!!\033[0m")
        return False
    # If the item code and category match, return True
    else:
        return True

# Function to write to file. Arguments passed are: the name of file to be written, the type of instruction for the function, and the data for the specific instruction
def writeFile(filename, mode, data):             
    match mode.upper():                 # For the kind of change that is to be made to the file, use match statement
        case "A":                       # If the change is to add an item
            with open(filename, 'a') as fil:                                    # Open the csv file in append mode, the with loop will automatically close the file
                fil.write(f"{data[0]:<15}{data[1]:<15}{data[2]:<15}{data[3]:<15}{data[4]:<15}\n")
        case "D":                       # If the change is to delete an item from the file   
            lines = readFile(filename)                                          # Read the file and store the lines in a list
            with open(filename, 'w') as fil:                                    # Open the file in write mode, the with loop will automatically close the file
                for line in lines:                                              # Loop through the list of lines
                    if not line.startswith(data):                               # If the line does not start with the item code, write the line to the file
                        fil.write(line)
            print("\033[92mItem deleted successfully!\033[0m")
        case "U":                       # If the change is to update an item in the file
            lines = readFile(filename)
            with open(filename, 'w') as fil:                                    # Open the file in write mode, the with loop will automatically close the file
                for line in lines:                                              # Loop through the list of lines
                    if line.startswith(data[0]):                                # If the line starts with the item code, write the updated line to the file
                        fil.write(f"{data[0]:<15}{data[1]:<15}{data[2]:<15}{data[3]:<15}{data[4]:<15}\n")
                    else:                                                       # If the line does not start with the item code, write the line to the file
                        fil.write(line)
            print("\033[92mItem updated successfully!\033[0m")
                       
def unpackFile():                                   # Function to return the list of lists from the file
    lines = readFile("inventory_Prajwal.txt")       # Read the lines from the file
    # Remove the header from the list of lines
    lines.pop(0)
    lines = [i.strip() for i in lines]              # Strip the lines of empty spaces at the start and end
    elmntList = [i.split() for i in lines]          # Split the each line into a list of its elements within the list
    elmntList = [[i[0], i[1], i[2], float(i[3]), int(i[4])] for i in elmntList] # Convert the strings to their respective data types
    return elmntList                                # Return the list of lists

def readFile(filename):
    try:
        with open(filename, 'r') as fil:            # Open the file in read mode, the with loop will automatically close the file
            return fil.readlines()                  # Read all the lines in the file
    except FileNotFoundError:
        print("\033[91mErro: No File to Read!!\033[0m")
        sys.exit("\033[93mExiting the program!!\033[0m")

# Function to check for previously created inventory file, if not present create one
def log_check():
    check = exists("inventory_Prajwal.txt")         # Check if the file exists
    if not check:                                   # Check if the file does not exist
        inventory = [
            ["F01", "Orange", "Fruit", 2.99, 1000], 
            ["F02", "Apple", "Fruit", 1.99, 5000],
            ["F03", "Banana", "Fruit", 1.5, 490],
            ["D01", "Milk", "Dairy", 7.5, 500],
            ["D02", "Cheese", "Dairy", 15, 840],
            ["D03", "Yogurt", "Dairy", 5.5, 700],
            ["V01", "Carrot", "Vegetable", 3.8, 890],
            ["V02", "Celery", "Vegetable", 3.99, 990],
            ["V03", "Bean", "Vegetable", 4.5, 1500],
            ["V04", "Potato", "Vegetable", 6, 1000],
            ]
        with open ("inventory_Prajwal.txt", 'w') as fil:
            fil.write(f"{'Item Code':<15}{'Item Name':<15}{'Category':<15}{'Price(CA$)':<15}{'Quantity':<15}\n")
            fil.writelines(f"{i[0]:<15}{i[1]:<15}{i[2]:<15}{i[3]:<15}{i[4]:<15}\n" for i in inventory)
    else:                                           # If the file exists, read from the inventory file
        pass
    
# Calling the main function
if __name__ == "__main__":
    main()