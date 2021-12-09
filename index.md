Andrew Kehl
12/7/21
UW Foundations in programming
Assignment 08
https://github.com/kehlstorm/IntroToProg-Python-Mod08/blob/main/Assignment_08.py

Introduction
The objective of this assignment is to read and understand the pseudo-code provided and then add code to make the application work. Pseudo-code requirements include: Load data from a file into a list of product objects when the script starts. Show the user a menu of options. Get the users menu option choice. Show the user the current data in the list of product objects. Let the user add data to the list of product objects. Let the user save current data to file and exit.    
 
Assignment08_AK.py
Assignment08_AK.py is a simple program that Reads data from a text file, Shows the user a menu of options. Gets the users menu option choice. Shows the user the current data in the list of product objects. Lets the user add data to the list of product objects. And finally, lets the user save current data to file and exit. I’ve also included ‘Remove an Item’ for review. 

Initially, the program reads data from the file ‘products.txt’ (Figure 1.0 & Figure 1.1) and then writes it onto a list in the program memory. The program then prints the data and then goes onto the Main Menu.

Figure 1.0 - Read Data

Figure 1.1 - Read Data from a File

Figure 1.2 - Print current data.

Main Menu
The main Menu was created with a while(True) loop. Starting with the menu tasks (Figure 2.0 & Figure 2.1) and then creating a menu choice command (Figure 2.0 & 2.2) 


Figure 2.0 Main Menu

Figure 2.1 - Print menu tasks

Figure 2.2 - Input menu choice

Figure 2.3 - Main menu user interface


1) Add an Item
For adding an item to the list, the program will run an input code asking for the item and cost. (Figure 3.0 and Figure 3.1) Next the program processes the data and adds it to the list. (Figure 3.0 and figure 3.2)

Figure 3.0 - Add an item

Figure 3.1 - Input item and cost

Figure 3.2 - Add data to a list

Figure 3.3 - Input user interface
2) Remove an item
For removing an item, the program will print the current data on the list (Figure 1.2), then ask for an input. (Figure 4.0 and Figure 4.1) If the input matches anything on the list, the program will remove it. (Figure 4.0 and Figure 4.2)

Figure 4.0 - Removing data

Figure 4.1 - Input item to remove

Figure 4.2 - Remove data from the list

Figure 4.3 - Removing data user interface

3) Show Current Data
For showing current data, the program will print the current data (Figure 1.2) but this time will run the file processor total_cost class which will sum up all of the values labeled ‘cost’. (Figure 5.0 and Figure 5.1)
Figure 5.0 - Show current data


Figure 5.1 - Total Cost


Figure 5.2 - Show current data user interface.


4) Save data and exit program
For save data and exit, the program will run yes/no choice instance and ask if the user wants to save the data to file. (Figure 6.0 and Figure 6.1) If the user chooses ‘y’, the program will run the write data to file instance and save the data. (Figure 6.0 and Figure 6.2) If ‘n’ or any other key is entered, the program will simply exit without saving. 


Figure 6.0 - Save data and exit program


Figure 6.1 - Yes/No choice input


Figure 6.2 Write data to a file

Conclusion
Assignment08_AK.py is a simple program that Reads data from a text file, Shows the user a menu of options. Gets the users menu option choice. Shows the user the current data in the list of product objects. Lets the user add data to the list of product objects. And finally, lets the user save current data to file and exit. I’ve also included ‘Remove an Item’ for review. 
