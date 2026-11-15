from products import *
from helpers import *
from data import *

low_stock = None

def show_full_inventory():
    print("\n=========== FULL INVENTORY ===========")
    counter = 0
    for product in products:
        if product["stock"] > 0:
            print_product(product)
            counter += 1
    
    if counter == 0:
        print("\nInventory is empty.")
    else:
        print(f"\n{counter} products in inventory.")
    return

def search_product_in_inventory():
    search_product(True)
    return

def add_to_inventory():
    print("\n=========== ADD UINTS TO INVENTORY ===========")
    print("\nHow many units would you like to add?")
    units = get_units(add=True)

    print("\nFor which product?")
    product_id = get_product_id()

    update_product_stock(product_id, units)
    print(f"Added {units} units to product ID - {product_id}")
    return

def reduce_from_inventory():
    print("\n=========== REDUCE UNITS FROM INVENTORY ===========")
    print("\nHow many units would you like to reduce?")
    units = get_units(reduce=True)

    print("\nFor which product?")
    product_id = get_product_id()

    update_product_stock(product_id, units)
    print(f"Reduced {units} units from product ID - {product_id}")
    return

def display_out_of_stock():
    print("\n=========== OUT-OF-STOCK PRODUCTS ===========")
    counter = 0

    for product in products:
        if product["stock"] == 0:
            print_product(product)
            counter += 1
    
    print(f"\n{counter} out-of-stock products.")
    return

def display_low_stock():
    print("\n=========== LOW STOCK PRODUCTS ===========")
    counter = 0
    global low_stock
    if not low_stock:
        print("\nLow stock has not yet been set, would you like to set it now? (yes/no).")
        choice = string_choice("yes", "no")
        if choice == "yes":
            set_low_stock_threshold()
        else:
            return

    for product in products:
        if product["stock"] <= low_stock:
            print_product(product)
            counter += 1
        
    print(f"\n{counter} low stock products.")
    return

def set_low_stock_threshold():
    global low_stock
    print("\n--- Set low stock threshold ---")    
    low_stock = get_units(add=True)
    print(f"\nLow stock is now set to - {low_stock}.")
    return

def inventory_managment():
    back_to_main_menu = False
    while not back_to_main_menu:
        print("""
--------- INVENTORY MANAGEMENT ---------

1. Show full inventory
2. Search for a product in inventroy
3. Add units to inventory
4. Reduce units from inventory
5. Display out-of-stock products
6. Display products with low stock
7. Set a low stock threshold
8. Back to main menu
        """)

        choice = get_choice(8)

        if choice == 1:
            show_full_inventory()
        elif choice == 2:
            search_product_in_inventory()
        elif choice == 3:
            add_to_inventory()
        elif choice == 4:
            reduce_from_inventory()
        elif choice == 5:
            display_out_of_stock()
        elif choice == 6:
            display_low_stock()
        elif choice == 7:
            set_low_stock_threshold()
        elif choice == 8:
            back_to_main_menu = True
    
    return
