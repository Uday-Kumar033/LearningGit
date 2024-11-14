#Define the menu of restro
menu = {
    "Pizza" : 200,
    'Pasta': 30,
    'Burger': 25,
    'Salad': 10,
    'Roti': 5,
    'Dahi': 50,
    "Coffe": 80
}
#Greet
print("Welcome to python Restrorant")
print()
print("Pizza : Rs200\nPasta : Rs30\nBurger : Rs25\nSalad : Rs10\nRoti : Rs5\nDahi : Rs50\nCoffe : Rs80")
order_total = 0
item_1 = input("Enter the name of item :")
if item_1 in menu:
    order_total +=menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available yet , Please order something else")

another_order = input("Do you want to add another item ? (Yes/No)")
if another_order == "Yes":
    item_2 = input("Enter the name of second item =")
    if item_2 in menu:
        order_total +=menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} not available yet")
print(f"The total amount of item to pay is {order_total}")  