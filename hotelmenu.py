# DECLARATION OF MENU
menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Pancake': 100,
    'Coffee': 60,
    'Salad': 20
}

# GREET
print("Welcome to our restaurant!!")
print("Menu:")
for item, price in menu.items():
    print(f"{item}: Rs{price}")

bill = 0

# First order
item_1 = input("Enter the name of the item you want to order: ")
if item_1 in menu:
    bill += menu[item_1]
    print(f"Your item {item_1} has been added to your order.")
else:
    print(f"Ordered item {item_1} is not available!!")

# Additional order
order2 = input("Want something else? (yes/no): ").strip().lower()
if order2 == "yes":
    item_2 = input("Enter the name of the item you want to order: ")
    if item_2 in menu:
        bill += menu[item_2]
        print(f"Your item {item_2} has been added to your order.")
    else:
        print(f"Ordered item {item_2} is not available!!")

# Final bill
print(f"The total bill of your order is Rs{bill}")


