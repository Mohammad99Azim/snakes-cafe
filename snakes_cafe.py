
opining = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
"""

list = [
    "Coffee",    "Tea",
    "Unicorn Tears",    "Pie",
    "Cake",    "Ice Cream",
    "A Literal Garden",    "Meat Tornado",
    "Steak",    "Salmon",
    "Spring Rolls",    "Cookies",
    "Wings"
]

orders = {}

print(opining)
var = None
while var != "quit":
    var = input("> ")
    if var in list:
        if var in orders:
            orders[var] += 1
        else:
            orders[var] = 1
        print("**  {0} order of {1} have been added to your meal **".format(orders[var], var))
    elif var == "quit":
        for x in orders:
            print("**  {0} order of {1} **".format(orders[x], x))
    else:
        print("Sorry We Don't Have That :(")