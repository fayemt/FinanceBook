# Imports
import math
import subprocess
from decimal import Decimal, InvalidOperation
from dataclasses import dataclass
from datetime import datetime 
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

"""
menu_subtitle = 'Hello and welcome to the Fallible Financial Tools Expense Tracker, Please select an option below:'




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
# setting the default categories
allowed_categories = {"food", "gas", "groceries", "subscriptions", "utilities"}

### Classes
# Defining Expenses
@dataclass
class Expense:
     amount: Decimal
     category: str
     description: str
     date: date
     
     # Creating an expense from inputs
     @classmethod
     def new_expense(cls, cln_amount, cln_category, cln_description, cln_date):
        return cls(amount=cln_amount, category=cln_category, description=cln_description, date=cln_date)



### Functions

def main():
    return start_terminal_menu()

#making an brute force clear command
def clear_screen():
    print("\033[2J\033[H", end="", flush=True)
    if os.name == 'nt':
        subprocess.run('cls', shell=True, check=False)
    else:
        subprocess.run('clear', shell=True, check=False)


## sanitizing functions

#sanitize amount. attempts to convert user input to decimal or returns none and error
def Sanitize_amount(raw_amount: str):
    #check if formatted correctly
     try:
         cln_amount = Decimal(raw_amount.strip().replace("$", ""))
         return cln_amount, "01. Currency format parsed successfully"
     except InvalidOperation:
         #no number + error code
         return None, "11. Invalid currency format"

#sanitize category. checks if allowed or returns none and error
def Sanitize_category(raw_category: str):
    cln_category = raw_category.strip().lower()
    if cln_category in allowed_categories:
        return cln_category, "02. category allowed"
    elif input('Category not found, would you like to add it? Y/n').strip().lower() not in ('n', 'no'):
        allowed_categories.add(cln_category)
        return cln_category, "02. category allowed"
    else:      
        return None, "12. category not found"

#sanitize date. utilizes black magic to read user input as date sometimes or returns none and error
def Sanitize_date(raw_date: str):
    for date_format in allowed_date_formats:
        try:
            return datetime.strptime(raw_date.strip(), date_format).date(), "03. Date format parsed successfully"
        except ValueError:
            return None, "13. Date format not allowed"

#etc
def Sanitize_description(raw_description: str):
    if raw_description.isprintable():
        return raw_description.strip(), "04. Desctiption allowed"
    else: 
        return None, "14. Description Invalid"


# User field input dictionary
field_config = {
    "amount": {
        "Sanitizer": Sanitize_amount,
        "prompt": "Expense amount: $",
        "note": " Please note, negative expenses are treated as Income."
    },

    "category": {
        "Sanitizer": Sanitize_category,
        "prompt": "Expense category: ",
        "note": ""
    },

    "date": {
        "Sanitizer": Sanitize_date,
        "prompt": "Expense date: ",
        "note": ""
    },
    "description": {
        "Sanitizer": Sanitize_description,
        "prompt": "Expense description: ",
        "note": ""
    },
}





## User input function
def user_get_expense_field(Field):
    Field_confirmed = False
    runcode = None
    field_info = field_config[Field]

    while not Field_confirmed:
        #reset screen + display text
        clear_screen()
        print(title_splash)
        print('Please enter the ' + Field + '.' + field_info.get("note"))
        if runcode is not None: print(runcode)

        #get UI + sanitize + set error code
        raw_Field = input(field_info["prompt"])
        cln_Field, runcode = field_info["Sanitizer"](raw_Field)
        if cln_Field is None:
            clear_screen()
            continue
        else:
            Field_confirmed = True

    return cln_Field # type: ignore - false positive, cln_Field is guaranteed to be not None here


#menu functions
def terminal_add_expense():
    #cleanup values
    cln_amount = None
    cln_category = None
    cln_description = None
    cln_date = None

    #obtain human input
    cln_amount = user_get_expense_field('amount')
    cln_category = user_get_expense_field('category')
    cln_description = user_get_expense_field('description')
    cln_date = user_get_expense_field('date')

    #create new expense
    Expense.new_expense(cln_amount, cln_category, cln_description, cln_date)
    start_terminal_menu()   
    return

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
    "Quit": quit
}

#main menu loop
def start_terminal_menu():
        clear_screen()
        #show title title_splash and call the menu helper
        print(title_splash)
        print(menu_subtitle)
        return menu_helper(main_menu)
#menu helper displays a menu dictionary and takes user input to chose a function
def menu_helper(selected_menu):
    menu_options = list(selected_menu.keys())

    while True:
        #list the menu options
        for index, item in enumerate(menu_options):
            print(f"{index + 1}. {item}")

        #ask for selection
        user_input = input("Choose a menu option #: ").strip()

        if user_input.isdigit():
            choice = int(user_input)

            if 1 <= choice <= len(menu_options):
                selected_key = menu_options[choice - 1]
                menu_function = selected_menu[selected_key]
                clear_screen()
                menu_function()
                return
            else:
                print(f"14. Choose a number between 1 and {len(menu_options)}.")
                continue
        else:
            print("15. Input must be a valid number.")
            continue
        









main()