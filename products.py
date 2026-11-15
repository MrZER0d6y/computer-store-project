from helpers import *
from data import *


def add_product():
    product = {
        "id": create_unique_id(product=True),
        "name": get_product_name(),
        "category": get_product_category(),
        "price": get_product_price(),
        "stock": get_initial_stock_quantity(),
        "active": True
    }
    products.append(product)
    print(f"\nProuct ({product["id"]}) added successfully")

def display_all_products():
    if not products:
        print("\nNo products founds.")
        return
    print("\n=========== PRODUCTS ===========")
    for product in products:
        print_product(product)
    return

def search_product_by_id(inventory):
    product_id = get_product_id()
    print(f"\n--- Product found (by ID - {product_id}) ---")
    for product in products:
        if inventory:
            if product["id"] == product_id and product["stock"] > 0 and product["active"] == True:
                print_product(product)
        else:
            if product["id"] == product_id:
                print_product(product)
    return

def search_product_by_name(inventory):
    product_name = get_product_name().lower()
    print(f"\n--- Products found (by name - {product_name}) ---")
    for product in products:
        if inventory:
            if product_name in product["name"].lower() and product["stock"] > 0 and product["active"] == True:
                print_product(product)
        else:
            if product_name in product["name"].lower():
                print_product(product)
    return

def search_product_by_category(inventory):
    product_category = get_product_category().lower()
    print(f"\n--- Products found (by category - {product_category}) ---")
    for product in products:
        if inventory:
            if product["category"].lower() == product_category and product["stock"] > 0 and product["active"] == True:
                print_product(product)
        else:
            if product["category"].lower() == product_category:
                print_product(product)
    return

def search_product(inventory=False):
    print("""
=========== SEARCH PRODUCT ===========

1. By ID
2. By Name
3. By Category
    """)

    choice = get_choice(3)
    
    if choice == 1:
        search_product_by_id(inventory)
    elif choice == 2:
        search_product_by_name(inventory)
    elif choice == 3:
        search_product_by_category(inventory)

    return

def update_product_stock(prodcut_id, units):
    for product in products:
        if product["id"] == prodcut_id:
            if product["stock"] + units < 0:
                print(f"\nCannot update stock - low stock (units - {units}, stock - {product["stock"]}).")
                return
            product["stock"] += units
            return

def update_product_name(product_id):
    product_name = get_product_name()
    for product in products:
        if product["id"] == product_id:
            product["name"] == product_name
            print(f"\nName of prodcut ID {product["id"]} updated successfully.")
            return

def update_product_category(product_id):
    product_category = get_product_category()
    for product in products:
        if product["id"] == product_id:
            product["category"] == product_category
            print(f"\nCategory of prodcut ID {product["id"]} updated successfully.")
            return

def update_product_price(product_id):
    product_price = get_product_price()
    for product in products:
        if product["id"] == product_id:
            product["price"] == product_price
            print(f"\nPrice of prodcut ID {product["id"]} updated successfully.")
            return

def update_product_status(product_id):
    product_status = get_product_status()
    for product in products:
        if product["id"] == product_id:
            product["active"] == product_status
            print(f"\nStatus of prodcut ID {product["id"]} updated successfully.")
            return

def update_product():
    print("""
=========== UPDATE PRODUCT ===========

1. Update name
2. Update category
3. Update price
4. Update status
    """)

    choice = get_choice(4)
    print("\nWhich product do you want to update?")
    product_id = get_product_id()

    if choice == 1:
        update_product_name(product_id)
    elif choice == 2:
        update_product_category(product_id)
    elif choice == 3:
        update_product_price(product_id)
    elif choice == 4:
        update_product_status(product_id)
    return

def delete_product():
    print("\n=========== DELETE PRODUCT ===========")
    print("\nWhich product do you want to delete?")
    product_id = get_product_id()
    print(f"\nYou sure you want to delete product ID {product_id} (yes/no)? ")
    choice = string_choice("yes", "no")
    if choice == "no":
        print(f"\nDeleting of product ID {product_id} canceled.")
        return
    products.pop(product_id - 1)
    print(f"\nProduct (ID: {product_id}) deleted successfully.")
    return

def product_managment():
    back_to_main_menu = False
    while not back_to_main_menu:
        print("""
--------- PRODUCTS MANAGEMENT ---------

1. Add Product
2. Display All Products
3. Search Product
4. Update Product
5. Delete Product
6. Back to Main Menu
        """)

        choice = get_choice(6)
    
        if choice == 1:
            add_product()
        elif choice == 2:
            display_all_products()
        elif choice == 3:
            search_product()
        elif choice == 4:
            update_product()
        elif choice == 5:
            delete_product()
        elif choice == 6:
            back_to_main_menu = True
    
    return
