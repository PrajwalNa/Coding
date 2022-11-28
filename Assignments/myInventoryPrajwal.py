"""
Assignment No.: 3
Course: PROG12974
Name: Prajwal Nautiyal
Sheridan Student Number: 991662442
Submission date: 27 November 2022
Instructor's name: Syed Tanbeer
------------------------------------------------------------------------------------------------------------------------
Inventory Management System (IMS), to demonstrate the use of dictionaries and file handling
The code checks if the inventory.csv file exists, if not, it creates a new file and writes the dictionary to it
Please ignore the "File saved successfully" message on the first run with as there is no file to read from
If the inventory.csv exists, the program will read the data from the csv file and update the dictionary accordingly
------------------------------------------------------------------------------------------------------------------------
ANSI codes used for colored output: 
033[91m - Red
033[92m - Green
033[93m - Yellow
033[94m - Blue
033[96m - Cyan
"""


import re                           # Importing the regular expression module
import sys                          # Importing the sys module to exit the program
import time                         # Importing the time module
import csv                          # Importing the csv module to read and write to the csv file
from os.path import exists

# Initialize the inventory dictionary
inventory = {
            "F01": ["Orange", "Fruit", 2.99, 1000], 
            "F02": ["Apple", "Fruit", 1.99, 5000],
            "F03": ["Banana", "Fruit", 1.5, 490],
            "D01": ["Milk", "Dairy", 7.5, 500],
            "D02": ["Cheese", "Dairy", 15, 840],
            "D03": ["Yogurt", "Dairy", 5.5, 700],
            "V01": ["Carrot", "Vegetable", 3.8, 890],
            "V02": ["Celery", "Vegetable", 3.99, 990],
            "V03": ["Bean", "Vegetable", 4.5, 1500],
            "V04": ["Potato", "Vegetable", 6, 1000],
            }

# Main Function
def main():
    log_check()
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
    except ValueError:              # If the user enters a non-integer value
        print("\033[91mPlease enter a number!!\033[0m")
        return getinput()           # Call the function again to get the input

# Routing function to direct the user to their desired choice    
def Route(choice : int):
    match choice:
        case 1:                     # Display all items
            op1()
        case 2:                     # Look up an item in the Inventory
            op2()
        case 3:                     # Add a new item to the Inventory
            op3()
        case 4:                     # Update an item in the Inventory
            op4()
        case 5:                     # Delete an item from the Inventory
            op5()
        case 6:                     # Find items by Category
            op6()
        case 7:                     # Item Count and Average price by Category
            op7()
        case 8:                     # Most Expensive Item by Category
            op8()
        case 9:                     # Total Price of each item in the Inventory
            op9()
        case 10:                    # Exit, using a carriage return to print the exit message one character per 0.02 seconds
            temp = ""
            for c in "Thank you for using the Inventory Database System":
                temp += c
                print(f"\033[92m\r{temp}",end="")
                time.sleep(0.02)
            print("\033[0m")
            sys.exit()              # Exit call from the sys module
        case _:                     # If the user enters a choice other than the ones mentioned above
            print("\033[91mPlease enter a valid option!!\033[0m")
            # Using recursion to call the function again to get the input in case of an invalid choice, instead of using a loop
            choice = getinput()
            Route(choice)

# Option 1: Display all items           
def op1():
    print(f"\n\033[96m{'*'*30} Displaying all items {'*'*30}")
    # Printing the header
    print(f"{'Item Code':<15}{'Item Name':<15}{'Category':<15}{'Price (CA$)':<15}{'Quantity':<15}")  
    print(f"{'-'*75}")              # Printing the header separator
    for key in inventory:           # Loop through the dictionary and print the values in a tabular format
        print(f"{key:<15}{inventory[key][0]:<15}{inventory[key][1]:<15}{inventory[key][2]:<15}{inventory[key][3]:<15}")
    print("\033[0m")

# Option 2: Look up an item in the Inventory
def op2():
    print(f"\n\033[96m{'*'*30} Look up an item in the Inventory {'*'*30}\033[0m")
    itemcode = input("Enter the item code: ").upper()
    # Convert the item code to uppercase to match the dictionary keys
    if itemcode in inventory:       # Check if the item code exists in the dictionary
        # Printing the header
        print(f"\033[96m{'Item Code':<15}{'Item Name':<15}{'Category':<15}{'Price (CA$)':<15}{'Quantity':<15}")
        print(f"{'-'*75}")          # Printing the header separator
        # Printing the values in a tabular format
        print(f"{itemcode:<15}{inventory[itemcode][0]:<15}{inventory[itemcode][1]:<15}{inventory[itemcode][2]:<15}{inventory[itemcode][3]:<15}\033[0m")
    else:                           # If the item code does not exist in the dictionary
        print("\033[91mItem not found\033[0m")

# Option 3: Add a new item to the Inventory
def op3():
    print(f"\n\033[96m{'*'*30} Add a new item to the Inventory {'*'*30}\033[0m")
    itemcode = input("Enter the item code: ").upper()                           # Convert the item code to uppercase to match the dictionary keys
    # Check if the item code is in the correct format using regex
    if re.match(r"^(F|V|D){1}[0-9]{2,3}$", itemcode):
        if itemcode in inventory:   # Check if the item code exists in the dictionary
            print("\033[94mItem already exists\033[0m")
        else:                       # If the item code does not exist in the dictionary
            try:
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
                        inventory[itemcode] = [itemname, category, price, quantity]
                        print("\033[92mItem added successfully\033[0m\n")
                        consent = input("\033[93mDo you want to save the changes in the file? (Y/N): \033[0m")
                        write(consent)                                          # Call the function to write the data to the csv file
            except ValueError:      # If the user enters a non-integer value for quantity or a non-float value for price
                print("\033[91mIllegal value entered!!\033[0m")
    else:                           # If the item code is not in the correct format
        print("\033[91mPlease enter a valid item code\033[0m")
        print("\033[91mItem code should be in the format [F/V/D][0-9][0-9][0-9]\033[0m")

# Option 4: Update an item in the Inventory
def op4():
    print(f"\n\033[96m{'*'*30} Update an item in the Inventory {'*'*30}\033[0m")
    itemcode = input("Enter the item code: ").upper()
    # Convert the item code to uppercase to match the dictionary keys
    if itemcode in inventory:       # Check if the item code to be updated exists in the dictionary
        print("\033[94mIf you don't want to change either the Name or Category of the Item leave the Input Empty.\
        \nThis should not be done with price and quantity, you will need to re-enter the value even if you don't want to change it\033[0m")
        try:                        # Try to update the item
            itemname = input("Enter the name: ").capitalize()
            if itemname == "":      # If the user does not want to change the name
                itemname = inventory[itemcode][0]                               # Set the name to the current name
            category = input("Enter the category: ").capitalize()               # Capitalising the first letter of category to match the dictionary format
            if category == "":      # If the user does not want to change the category
                category = inventory[itemcode][1]                               # Set the category to the current category
            # Check if the category is valid
            while not validate(category):
                print("\033[91mInvalid category\033[0m")
                print("\033[94mValid categories are: Fruit, Vegetable, Dairy\033[0m")
                category = input("Enter the item category: ").capitalize()   
            else:
                # Checking if the category does not match the itemcode, else update the item in the dictionary
                if match(itemcode, category):
                    price = float(input("Enter the price: "))
                    quantity = int(input("Enter the quantity: "))
                    inventory.update({itemcode : [itemname, category, price, quantity]})
                    # Open the file in write mode, using 'r' to avoid escaping the backslash in the file path
                    print("\033[92mItem updated successfully\033[0m\n")
                    consent = input("\033[93mDo you want to save the changes in the file? (Y/N): \033[0m")
                    write(consent)  # Call the function to write the data to the csv file
        except ValueError:          # If the user enters a non-integer value for quantity or a non-float value for price
            print("\033[91mIllegal value entered!!\033[0m")
    else:                           # If the item code to be updated does not exist in the dictionary
        print("\033[91mItem not found\033[0m")

# Option 5: Delete an item from the Inventory
def op5():
    print(f"\n\033[96m{'*'*30} Delete an item from the Inventory {'*'*30}\033[0m")
    itemcode = input("Enter the item code: ").upper()                           # Convert the item code to uppercase to match the dictionary keys
    # Check if the item code to be deleted exists in the dictionary, else print the error message
    if itemcode in inventory:
        del inventory[itemcode]
        print("\033[92mItem deleted successfully\033[0m\n")
        cnst = input("\033[93mDo you want to save the changes in the file? (Y/N): \033[0m").upper()
        write(cnst)                     # Call the function to write the data to the csv file
    else:
        print("\033[91mItem not found\033[0m")

# Option 6: Find items by Category
def op6():
    print(f"\n\033[96m{'*'*30} Find items by Category {'*'*30}\033[0m")
    category = input("Enter the category: ").capitalize()                       # Capitalising the first letter of category to match the dictionary format
    # Checking if the category is valid, else print error message
    if validate(category):
        # Printing the header
        print(f"\033[96m{'Item Code':<15}{'Item Name':<15}{'Price (CA$)':<15}{'Quantity':<15}")
        print(f"{'-'*60}")          # Print the header separator
        for key in inventory:       # Loop through the dictionary and print the values (excluding category) in a tabular format
            # Checking if the category matches the category entered by the user
            if inventory[key][1] == category:
                print(f"{key:<15}{inventory[key][0]:<15}{inventory[key][2]:<15}{inventory[key][3]:<15}")
        print("\033[0m")
    else:
        print("\033[91mPlease enter a valid category!!\033[0m")

# Option 7: Printing Item Count and Average Price of each Category
def op7():
    fruitcount = 0                  # Initialize the fruit count to 0
    fruitprice = 0.0                # Initialize the fruit price to 0
    dairycount = 0                  # Initialize the dairy count to 0
    dairyprice = 0.0                # Initialize the dairy price to 0
    vegcount = 0                    # Initialize the vegetable count to 0
    vegprice = 0.0                  # Initialize the vegetable price to 0
    for key in inventory:           # Loop through the dictionary and calculate the item count and total price of items in each category
        # If the category is Fruit, increment the fruit count and add the price to the fruit price
        if inventory[key][1] == "Fruit":
            fruitcount += 1
            fruitprice += inventory[key][2]
        # If the category is Dairy, increment the dairy count and add the price to the dairy price
        elif inventory[key][1] == "Dairy":
            dairycount += 1
            dairyprice += inventory[key][2]
        # If the category is Vegetable, increment the vegetable count and add the price to the vegetable price
        elif inventory[key][1] == "Vegetable":
            vegcount += 1
            vegprice += inventory[key][2]
    # Calculating the average price of each category
    avgfruitprice = fruitprice / fruitcount
    avgdairyprice = dairyprice / dairycount
    avgvegprice = vegprice / vegcount
    print(f"\n\033[96m{'*'*30} Printing Item Count and Average Price of each Category {'*'*30}")
    # Printing the header
    print(f"{'Category':<15}{'Item Count':<15}{'Average Price (CA$)':<20}")
    print(f"{'-'*50}")              # Print the header separator
    # Printing the item count and average price of each category in a tabular format
    print(f"{'Fruit':<15}{fruitcount:<15}{avgfruitprice:<20}\
            \n{'Dairy':<15}{dairycount:<15}{avgdairyprice:<20}\
            \n{'Vegetable':<15}{vegcount:<15}{avgvegprice:<20}\033[0m")

# Option 8: Most Expensive Item for each Category
def op8():
    maxFruit = 0.0                  # Initialize the maximum fruit price to 0
    maxDairy = 0.0                  # Initialize the maximum dairy price to 0
    maxVeg = 0.0                    # Initialize the maximum vegetable price to 0
    FruitID = ""                    # Initialize the fruit item code to an empty string
    DairyID = ""                    # Initialize the dairy item code to an empty string
    VegID = ""                      # Initialize the vegetable item code to an empty string
    for item in inventory:          # Loop through the dictionary and find the maximum price of each category
        # If the category is Fruit and the price is greater than the maximum fruit price, update the maximum fruit price and fruit item code
        if inventory[item][1] == "Fruit":
            if inventory[item][2] > maxFruit:
                maxFruit = inventory[item][2]
                FruitID = item
        # If the category is Dairy and the price is greater than the maximum dairy price, update the maximum dairy price and dairy item code
        elif inventory[item][1] == "Dairy":
            if inventory[item][2] > maxDairy:
                maxDairy = inventory[item][2]
                DairyID = item
        # If the category is Vegetable and the price is greater than the maximum vegetable price, update the maximum vegetable price and vegetable item code
        elif inventory[item][1] == "Vegetable":
            if inventory[item][2] > maxVeg:
                maxVeg = inventory[item][2]
                VegID = item
    print(f"\n\033[96m{'*'*30} Most Expensive Item for each Category {'*'*30}")
    # Printing the header
    print(f"{'Category':<15}{'Item Code':<15}{'Item Name':<15}{'Price (CA$)':<15}")
    print(f"{'-'*60}")              # Printing the header separator
    print(f"{'Fruit':<15}{FruitID:<15}{inventory[FruitID][0]:<15}{inventory[FruitID][2]:<15}\
            \n{'Dairy':<15}{DairyID:<15}{inventory[DairyID][0]:<15}{inventory[DairyID][2]:<15}\
            \n{'Vegetable':<15}{VegID:<15}{inventory[VegID][0]:<15}{inventory[VegID][2]:<15}\033[0m")

# Option 9: Total Price of each item in the Inventory
def op9():
    print(f"\n\033[96m{'*'*30} Total Price of each item in the Inventory {'*'*30}")
    # Printing the header
    print(f"{'Item Code':<15}{'Item Name':<15}{'Total Price (CA$)':<20}")
    print(f"{'-'*60}")              # Printing the header separator
    for key in inventory:           # Loop through the dictionary and print the values (excluding category) in a tabular format
        print(f"{key:<15}{inventory[key][0]:<15}{inventory[key][2] * inventory[key][3]:<20}")
    print("\033[0m")

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

# Function to store the dictionary in a file
def write(consent):             
    match consent.upper():          # Checking if the user wants to save the dictionary using match statement
        case "Y":
            with open("inventory.csv", mode='w') as fil:                                            # Open the csv file in write mode
                fields = ["Item Code", "Item Name", "Category", "Price (CA$)", "Quantity"]          # List of fields
                csvW = csv.DictWriter(fil, fieldnames=fields)                                       # Create a csv dictionary writer object
                csvW.writeheader()                                                                  # Write the header
                # Loop through the dictionary and write the values in the csv file
                csvW.writerows([{"Item Code": k, "Item Name": v[0], "Category": v[1], "Price (CA$)": v[2], "Quantity": v[3]} for k, v in inventory.items()])
            fil.close()                                                                             # Close the file
            print("\033[92mFile saved successfully!\033[0m")
        case "N":
            print("\033[94mChanges not saved in the file!!\033[0m")
        case _:                     # If the user enters anything other than Y or N, print the error message
            print("\033[91mPlease Choose Either 'Y' or 'N'\033[0m")
            write(input("\033[93mDo you want to save the changes in the file? (Y/N): \033[0m"))
    
# Function to check for previously created inventory file, if it is created it will update the dictionary from the file
def log_check():
    check = exists("inventory.csv") # Check if the file exists
    if not check:                   # Check if the csv file does not exist
        write("Y")                  # Write the dictionary to the csv file
    else:                           # If the csv file exists, read from the inventory file
        # Creating csv dictorionary reader object
        read = csv.DictReader(open("inventory.csv"))
        # Unpacking the csv file into the dictionary with itereating over the rows
        newinpt = {rows["Item Code"]: [rows["Item Name"], rows["Category"], rows["Price (CA$)"], rows["Quantity"]] for rows in read}
        inventory.update(newinpt)   # Updating the dictionary with the new values
        # Deleting the dictionary keys that are not in the csv file
        for key in inventory.keys():
            if key not in newinpt.keys():
                del inventory[key]
            
# Calling the main function
if __name__ == "__main__":
    main()