from helpers import *

def calculate_subtotal():
    pass

def calculate_discount():
    pass

def calculate_total():
    pass

def sale_summary(sale):
    print("\n=========== SALE SUMMARY ===========")

    for item in sale["items"]:
        print(f"{item["name"]:<10}{item["quantity"]} x {item["price"]} = {item["total"]}")

    print("\n------------------------------------\n")
    print(f"Subtotal: {sale["Subtotal"]}\nDiscount: {sale["discount"]}\nTotal: {sale["total"]}")
    print("====================================")
    print("Sale completed successfully!")
    return

def new_sale():
    print("\n=========== NEW SALE ===========")
    items = []

    complete_sale = False
    while not complete_sale:
        prodcut_id = get_product_id()
        quantity = get_units()

        item = {
            "product_id": prodcut_id,
            "name": products[prodcut_id - 1]["name"],
            "quantity": quantity,
            "unit_price": products[prodcut_id - 1]["price"],
            "total": products[prodcut_id - 1]["price"] * quantity
        }
        items.append(item)
        print("!Added to cart!")

        print("""
    1. Continue Shopping
    2. Complete Sale
    3. Cancel Sale
        """)

        choice = get_choice(3)

        if choice == 1:
            continue
        elif choice == 2:
            complete_sale = True
        elif choice == 3:
            print("\nSale canceled.")
            return

    sale = {
        "id": create_unique_id(sale=True),
        "items": items,
        "subtotal": calculate_subtotal(),
        "discount": calculate_discount(),
        "total": calculate_total(),
    }
    sales.append(sale)
    sale_summary(sale)
    return

def add_items_to_cart():
    pass

def update_product_quantity():
    pass

def remove_item_from_cart():
    pass

def checkout():
    pass

def update_inventory():
    pass

def save_sale():
    pass

def sales_managment():
    pass