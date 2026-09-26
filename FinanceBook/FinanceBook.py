# Imports
import math
from decimal import Decimal, InvalidOperation
from dataclasses import dataclass
from datetime import date
import os


### Variables

#determine start type
terminal_mode = 1

#record the title splash screen
title_splash = r"""
 /$$$$$$$$       /$$ /$$ /$$ /$$       /$$                 /$$$$$$$$ /$$                                         /$$           /$$       /$$$$$$$$                  /$$          
| $$_____/      | $$| $$|__/| $$      | $$                | $$_____/|__/                                        |__/          | $$      |__  $$__/                 | $$          
| $$    /$$$$$$ | $$| $$ /$$| $$$$$$$ | $$  /$$$$$$       | $$       /$$ /$$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$$ /$$  /$$$$$$ | $$         | $$  /$$$$$$   /$$$$$$ | $$  /$$$$$$$
| $$$$$|____  $$| $$| $$| $$| $$__  $$| $$ /$$__  $$      | $$$$$   | $$| $$__  $$ |____  $$| $$__  $$ /$$_____/| $$ |____  $$| $$         | $$ /$$__  $$ /$$__  $$| $$ /$$_____/
| $$__/ /$$$$$$$| $$| $$| $$| $$  \ $$| $$| $$$$$$$$      | $$__/   | $$| $$  \ $$  /$$$$$$$| $$  \ $$| $$      | $$  /$$$$$$$| $$         | $$| $$  \ $$| $$  \ $$| $$|  $$$$$$ 
| $$   /$$__  $$| $$| $$| $$| $$  | $$| $$| $$_____/      | $$      | $$| $$  | $$ /$$__  $$| $$  | $$| $$      | $$ /$$__  $$| $$         | $$| $$  | $$| $$  | $$| $$ \____  $$
| $$  |  $$$$$$$| $$| $$| $$| $$$$$$$/| $$|  $$$$$$$      | $$      | $$| $$  | $$|  $$$$$$$| $$  | $$|  $$$$$$$| $$|  $$$$$$$| $$         | $$|  $$$$$$/|  $$$$$$/| $$ /$$$$$$$/
|__/   \_______/|__/|__/|__/|_______/ |__/ \_______/      |__/      |__/|__/  |__/ \_______/|__/  |__/ \_______/|__/ \_______/|__/         |__/ \______/  \______/ |__/|_______/ 
                                                                                                                                                                                 
                                                                                                                                                                                 
                                                                                                                                                                                 
 /$$$$$$$$                                                                   /$$$$$$$$                           /$$                                                             
| $$_____/                                                                  |__  $$__/                          | $$                                                             
| $$       /$$   /$$  /$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$$  /$$$$$$          | $$  /$$$$$$  /$$$$$$   /$$$$$$$| $$   /$$  /$$$$$$   /$$$$$$                                    
| $$$$$   |  $$ /$$/ /$$__  $$ /$$__  $$| $$__  $$ /$$_____/ /$$__  $$         | $$ /$$__  $$|____  $$ /$$_____/| $$  /$$/ /$$__  $$ /$$__  $$                                   
| $$__/    \  $$$$/ | $$  \ $$| $$$$$$$$| $$  \ $$|  $$$$$$ | $$$$$$$$         | $$| $$  \__/ /$$$$$$$| $$      | $$$$$$/ | $$$$$$$$| $$  \__/                                   
| $$        >$$  $$ | $$  | $$| $$_____/| $$  | $$ \____  $$| $$_____/         | $$| $$      /$$__  $$| $$      | $$_  $$ | $$_____/| $$                                         
| $$$$$$$$ /$$/\  $$| $$$$$$$/|  $$$$$$$| $$  | $$ /$$$$$$$/|  $$$$$$$         | $$| $$     |  $$$$$$$|  $$$$$$$| $$ \  $$|  $$$$$$$| $$                                         
|________/|__/  \__/| $$____/  \_______/|__/  |__/|_______/  \_______/         |__/|__/      \_______/ \_______/|__/  \__/ \_______/|__/                                         
                    | $$                                                                                                                                                         
                    | $$                                                                                                                                                         
                    |__/                                                                                                                                                         

Hello and welcome to the Fallible Financial Tools Expense Tracker, or FFTET (pronounced FuHTeT), Please select an option below:
"""



#Date formats
allowed_date_formats = [
    "%m/%d/%Y", #12/31/1999
    "%m/%d/%y", #12/31/99
    "%Y/%m/%d", #1999/12/31

    "%m-%d-%Y", #12-31-1999
    "%m-%d-%y", #12-31-99
    "%Y-%m-%d", #1999-12-31

    "%m.%d.%Y", #12.31.1999
    "%m.%d.%y", #12.31.99
    "%Y.%m.%d", #1999.12.31
    ]
# setting the base catagories
allowed_catagories = {"food", "gas", "groceries", "subscriptions", "utilities"}


### Functions

#making an os agnostic clear command
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

#sanitizing functions
#sanitize amount. attempts to convert user input to decimal or returns none and error
def Sanitize_amount(raw_amount: str):
    #check if formatted correctly
     try:
         cln_amount = Decimal(raw_amount.strip().replace("$", ""))
         return cln_amount, "01. Currency format parsed successfully"
     except InvalidOperation:
         #no number + error code
         return None, "11. Error invalid currency format"

#sanitize catagory. checks if allowed or returns none and error
def Sanitize_catagory(raw_catagory: str):
    if raw_catagory in allowed_catagories:
        cln_catagory = raw_catagory
        return cln_catagory, "02. Catagory allowed"
    else:
        return None, "12. Catagory not found"

#sanitize date. attempts to read user input as date or returns none and error
def Sanitize_date(raw_date: str):
    for date_format in allowed_date_formats:
        try:
            return datetime.strptime(raw_date.strip(),"date_format").date(), "03. Date format parsed successfully"
        except ValueError:
            return None, "13. Date formate not allowed"

#menu functions
def terminal_add_expense():
    menu_state = "addexpense"
    return print("debug fail")

def terminal_view_expenses():
    return print("debug fail")

def terminal_total_expenses():
    return print("debug fail")

def terminal_options_menu():
    return print("debug fail")

#store the main menu items
main_menu = {
    "Add an Expense": terminal_add_expense,
    "View Expenses": terminal_view_expenses,
    "Total Expenses": terminal_total_expenses,
    "Options": terminal_options_menu,
    "Quit": quit
}
menu_options = list(main_menu.keys())

#main menu loop
def run_terminal_menus():
    menu_state = "main"
    while menu_state == "main":
        clear_screen()
        #show title title_splash
        print(title_splash)

        #actually list the menu options
        for index, item in enumerate(menu_options):
            print(f"{index + 1}. {item}")
            #ask for selection
        user_input = input("Choose a menu option number: ").strip()
        if user_input.strip().isdigit():
            choice = int(user_input.strip())
    
            if 1 <= choice <= len(menu_options):
                selected_key = menu_options[choice - 1]
                menu_function = main_menu[selected_key]
                menu_function()
            else:
                print(f"Error 14. Choose a number between 1 and {len(menu_options)}.")
                continue
        else:
            print("Error 15. Input must be a valid number.")
            continue
    return




#Terminal startup
def terminal_startup():
    run_terminal_menus()
    



### Classes
# Defining Expenses
@dataclass
class Expense:
     amount: Decimal
     catagory: str
     description: str
     date: date
     
     # Creating an expense from inputs
     @classmethod
     def new_expense(cls, cln_amount, cln_catagory, cln_description, cln_date):
        return cls(amount=cln_amount, category=cln_catagory, date=cln_date)
terminal_startup()