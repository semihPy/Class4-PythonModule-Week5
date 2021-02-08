'''
#############################################################################################
#*******************************************************************************************#
#           Copyright (c) 2020 pyCoder|semih Corporation;) All rights reserved.            ##
#                                   [Timestamp:20210208]                                   ##
#*******************************************************************************************#
#############################################################################################
'''
# Question 2:
# Define a class named ItemInfo with the following description:
#
# item_code(Item Code), item(item name), price(Price of each item), qty(quantity in stock),
# discount(Discount percentage on the item), net_price(Price after discount)
#
# Methods :
# A member method calculate_discount() to calculate discount as per the following rules:
# If qty <= 10 —> discount is 0
# If qty (11 to 20 inclusive) —> discount is 15
# If qty >= 20 —> discount is 20
# A constructor init method to assign the initial values for item_code to 0 and price, qty, net_price and discount to null
# A function called buy() to allow user to enter values for item_code, item, price, qty.
# Then call function calculate_discount() to calculate the discount and net_price(price * qty - discount).
# A function show_all() or similar name to allow user to view the content of all the data members.

class ItemInfo:
    def __init__(self, item_code=0, item=0, price=0, qty=0, discount=0, net_price=0):
        self.item_code = item_code
        self.item = item
        self.price = price
        self.qty = qty
        self.discount = discount
        self.net_price = net_price

    def calculate_discount(self):
        if int(self.qty) <= 10:
            self.discount = 0
        elif 11 <= int(self.qty) <= 20:
            self.discount = 15
        elif int(self.qty) >= 20:
            self.discount = 20
        net_price = int(self.price) * int(self.qty) - int(self.discount)
        return net_price

    def buy(self):
        self.item_code = input("Enter a Item Code:")
        self.item = input("Enter a item name:")
        self.price = input("Enter a price:")
        self.qty = input("Enter a quantity of stock:")
        ItemInfo.calculate_discount(self)

    def show_all(self):
        print("%%%%%%% All The Data Members %%%%%%%")
        print("Item Code        : {} "
              "\nitem name        : {} "
              "\nprice            : {} "
              "\nquantity in stock: {} "
              "\ndiscount         : {} "
              "\nnet_price        : {} "
              .format(self.item_code, self.item, self.price, self.qty, self.discount, ItemInfo.calculate_discount(self)))

x = ItemInfo()
x.buy()
x.calculate_discount()
x.show_all()
