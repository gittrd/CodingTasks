"""
1) Instantiating a list named "menu", containing four items.
2) Instantiating a dictionary called "stock", containing the stock value 
for the four items on the menu.
3) Creating a dictionary called "price", containing prices for each item
on the menu.
4) Computing the total stock worth in the cafe.
"""

# list containing the items in the cafe
menu = ["cofe", "water", "smoothie", "fruits"]

print(f"The menu list available is as follows: {menu}")

# dictionary containing the stock for the items in the menu
stock = {
    "cofe" : 20,
    "water" : 50,
    "smoothie" : 5,
    "fruits" : 50
}

print(f"The stock available is as follows: {stock}")

# dictionary containing the prices in the cafe
price = {
    "cofe" : 5.50,
    "water" : 2.15,
    "smoothie" : 3.65,
    "fruits" : 2.89
}

print(f"The prices are as follows: {price}")


# variable storing the total price from the loop
total_value = 0

# for looping that iterates through each item in the "menu" list, then calculates the price
for menu_item in menu:
    item_value = (stock[menu_item] * price[menu_item])
    total_value += item_value

print(f"The total stock worth in the cafe is: {total_value}")
