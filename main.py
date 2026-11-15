from inventory import *
from products import *

def main():
    exiting = False

    while not exiting:
        print("""
=================================
      COMPUTER STORE SYSTEM
=================================

1. Products Management
2. Inventory Management
3. Sales Management
4. Reports
5. Exit
        """)

        choice = get_choice(5)
        
        if choice == 1:
            product_managment()
        elif choice == 2:
            inventory_managment()
        elif choice == 3:
            sales_managment()
        elif choice == 4:
            reports()
        elif choice == 5:
            print("\nExiting...")
            exiting = True
    
    return 0

if __name__ == "__main__":
    main()