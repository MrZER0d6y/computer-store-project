from data import *

def create_unique_id(product=False, sale=False):
    if product:
        if not products:
            return 1
        return products[-1]["id"] + 1
    if sale:
        if not sale:
            return 1
        return sales[-1]["id"] + 1

def print_product(product):
    print(f"""
ID: {product["id"]}\nName: {product["name"]}\nCategory: {product["category"]}
Price: {product["price"]}\nStock: {product["stock"]}\nActive: {product["active"]}""")
    return

def get_choice(options):
    valid_choice = False
    while not valid_choice:
        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Choise must be integer, try again.")
            continue
        if choice < 1 or choice > options:
            print("Choise must be positive, try again.")
            continue
        valid_choice = True
    return choice

def get_product_id():
    valid_id = False
    while not valid_id:
        try:
            product_id = int(input("\nProduct ID: "))
        except ValueError:
            print("\nProduct ID must be integer, try again.")
            continue
        if product_id < 1:
            print("\nProduct ID must be positive, try again.")
            continue
        if product_id > len(products):
            print("\nProduct ID does not exists, try again.")
            continue
        valid_id = True
    return product_id

def get_product_name():
    valid_name = False
    while not valid_name:
        name = input("\nName: ")
        if not name:
            print("\nName cannot be empty, try again.")
            continue
        valid_name = True
    return name

def get_product_category():
    valid_category = False
    while not valid_category:
        category = input("\nCategory: ").capitalize()
        if not category:
            print("\nCategroy cannot be empty, try again.")
            continue
        if category not in VALID_CATEGORIES:
            print("\nNot a valid category, try again.")
            continue
        valid_category = True
    return category

def get_product_price():
    valid_price = False
    while not valid_price:
        try:
            price = float(input("\nPrice: "))
        except ValueError:
            print("\nPrice must be integer or float, try again.")
            continue
        if price < 1:
            print("\nPrice must be positive, try again.")
            continue
        valid_price = True
    return price

def get_initial_stock_quantity():
    valid_stock_quantity = False
    while not valid_stock_quantity:
        try:
            stock_quantity = int(input("\nInitial Stock Quantity: "))
        except ValueError:
            print("\nInitial stock quantity must be integerm, try again.")
            continue
        if stock_quantity < 0:
            print("\nInitial stock quantity cannot be negative, try again.")
            continue
        valid_stock_quantity = True
    return valid_stock_quantity

def get_units(add=False, reduce=False):
    valid_units_quantity = False
    while not valid_units_quantity:
        try:
            units = int(input("\nUnits: "))
        except ValueError:
            print("\nUnits must be integer, try again.")
            continue
        if add:
            if units < 1:
                print("\nUnits must be positive, try again.")
                continue
        if reduce:
            if units > -1:
                print("\nUnits must be negative, try again.")
                continue
        valid_units_quantity = True
    return units

def get_product_status():
    valid_status = False
    while not valid_status:
        status = input("\nStatus (true/false): ").lower()
        if status != "true" and status != "false":
            print("\nStatus must be true or false, try again.")
            continue
        valid_status = True
    return status

def string_choice(string1, string2):
    valid_string = False
    while not valid_string:
        string = input("\nEnter you choice: ").lower()
        if string != string1 and string != string2:
            print(f"\nChoice must be {string1}/{string2}, try again.")
            continue
        if string == string1:
            return string1
        return string2
            