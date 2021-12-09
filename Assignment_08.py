# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Andrew Kehl,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """
class FileReader:

    def ReadFileDataToString(self, file_name):
        lstOfProductObjects.clear
        product_object = Product('', 0)
        with open(file_name, 'r') as file:
            for line in file:
                name, price = line.split(', ')
                product_object = Product('', 0)
                product_object.item = item
                product_object.price = price
                lstOfProductObjects.append(product_object)
            return lstOfProductObjects

    pass
    # TODO: Add Code to the Product class
# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Andrew Kehl,11/30/21,Modified code to complete assignment 8
    """
    pass

    #Code to process data from a file
    @staticmethod
    def read_data_from_file(strFileName, list_of_rows):
        lstOfProductObjects.clear()  # clear current data
        file = open(strFileName, "r")
        for line in file:
            strItem, Cost, strLocation = line.split(",")
            row = {"Item": strItem.strip(), "Cost": Cost.strip(), "Location": strLocation.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows, 'Success'

    #Add Code to process data to a file
    def write_data_to_file(strFileName, list_of_rows):
        objFile = open(strFileName, "w")
        for row in list_of_rows:
            objFile.write(str(row["Item"]) + ', ' + str(row["Cost"]) + ', ' + str(row['Location'] + '\n'))
        print(" Data was saved to file: products.txt. ")
        objFile.close()
        return list_of_rows, 'Success'

    #Add data to a list.
    def add_data_to_list(strItem, Cost, strLocation, list_of_rows):
        dicRow = {"Item": strItem, "Cost": Cost, "Location": strLocation}
        list_of_rows.append(dicRow)
 #       for row in list_of_rows:
 #           print(row['Item'] + ' | $' + str(row['Cost']) + ' | ' + row['Location'])
        return list_of_rows, 'Success'

    #Code to remove data from a list.
    def remove_data_from_list(strItem, list_of_rows):
        for row in list_of_rows:
            if row["Item"].lower() == strItem.lower():
                list_of_rows.remove(row)
                print(strItem + " Removed from list")
        return list_of_rows, 'Success'


    def total_cost(list_of_rows):
        total_cost = 0
        for row in list_of_rows:
            total_cost += float(row['Cost'])
        return total_cost
# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    #Code to show menu to user
    def print_menu_Tasks():
        print('''
        *** Main Menu *** 
        1) Add an Item
        2) Remove an Item
        3) Show current Items
        4) Save Data & Exit Program        
        ''')
        print()  # Add an extra line for looks

    #Code to get user's choice
    def input_menu_choice():
        choice = str(input("Please select an option: [1 - 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    #Code to show the current data from the file to user
    def print_current_data():
        print('Current Data:')
        print('Item | Cost | Location')
        print('****************************************************')
        for row in lstOfProductObjects:
            print(row['Item'] + ' | ' + '$ '+ str(row['Cost']) + ' | ' + row['Location'])

    #Code to get product data from user
    def input_item_and_cost():
        print("Shopping List Data Entry")
        while (True):
            Item = input(" Enter an Item: ") #Item input with numeric error handling.
            if Item.isnumeric():
                print('Enter Only Items.')
                continue
            else:
                break


    Cost = float(input(" Enter a Cost: ")) #Cost input.

            Location = input(" Enter a Location: ") #Location input with numeric error handling.
            if Location.isnumeric():
                print('Enter Only Locations.')
                continue
            else:
                break
        return Item, Cost, Location

    def input_item_to_remove(lstOfProductObjects):
        remItem = input("Item to Remove: ")
        return remItem

    def input_press_enter():
        input('Press [Enter]to continue.')

    def input_yes_no_choice(message):
        return str(input(message)).strip().lower()


# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program

# Main Body of Script  ---------------------------------------------------- #
F=FileProcessor()

F.read_data_from_file(strFileName, lstOfProductObjects)  #Read file data
IO.print_current_data() #Print current file data
while(True):
    IO.print_menu_Tasks()
    strChoice = IO.input_menu_choice()
    if strChoice.strip() == '1':  # Add a new item
        strItem, Cost, strLocation = IO.input_item_and_cost()
        FileProcessor.add_data_to_list(strItem, Cost, strLocation, lstOfProductObjects)
        IO.input_press_enter()
        continue
    if strChoice.strip() == '2': # Remove an item
        IO.print_current_data()
        strItem = IO.input_item_to_remove(lstOfProductObjects)
        FileProcessor.remove_data_from_list(strItem, lstOfProductObjects)
        IO.input_press_enter()
        continue
    if strChoice.strip() == '3': # Show current data
        IO.print_current_data()
        print('****************************************************')
        print('Total Cost is: $', FileProcessor.total_cost(list_of_rows=lstOfProductObjects))
        print('****************************************************')
        IO.input_press_enter()
        continue
    if strChoice.strip() == '4': # Save data & Exit Program
        YNChoice = IO.input_yes_no_choice("Save this data to file? (y/n): ")
        if YNChoice.lower() == "y":
            FileProcessor.write_data_to_file(strFileName, lstOfProductObjects)
            print('Goodbye!')
            break
        else:
            print('Goodbye!')
            break

    else:
        print('This input is not valid.')
