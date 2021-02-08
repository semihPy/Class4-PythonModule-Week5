'''
#############################################################################################
#*******************************************************************************************#
#           Copyright (c) 2020 pyCoder|semih Corporation;) All rights reserved.            ##
#                                   [Timestamp:20210208]                                   ##
#*******************************************************************************************#
#############################################################################################
'''
# Question 3:
# Define a class named Product with the following specifications:
# Data members:
# 1-product_id – A string to store product.
# 2-product_name - A string to store the name of the product.
# 3-product_purchase_price – A decimal to store the cost price of the product.
# 4-product_sale_price – A decimal to store Sale Price Margin - A decimal to be calculated as (product_sale_price - product_purchase_price)
# 5-Remarks - To store "Profit" if Margin is positive else "Loss" if Margin is negative.
# Methods :
# A constructor to intialize all the data members with valid default values.
# A method set_remarks() that assigns Margin as (product_sale_price - product_purchase_price) and sets Remarks as mentioned below :
# Margin             Remarks
# < 0 (negative)     Loss
# > 0 (positive)     Profit
# A method set_details() to accept values for product_id, product_name, product_purchase_price, product_sale_price and invokes SetRemarks() method.
# A method get_details() that displays all the data members.

class Product:
    def __init__(self, product_id, product_name, product_purchase_price, product_sale_price, Remarks):
        self.product_id = product_id
        self.product_name = product_name
        self.product_purchase_price = float(product_purchase_price)
        self.product_sale_price = float(product_sale_price)
        self.Remarks = Remarks

    def set_remarks(self):
        margin = self.product_sale_price - self.product_purchase_price
        if margin < 0:
            return "Loss"
        else:
            return "Profit"

    def set_details(self):
        self.product_id = input("product_id: ")
        self.product_name = input("product_name: ")
        self.product_purchase_price = float(input("product_purchase_price: "))
        self.product_sale_price = float(input("product_sale_price: "))
        return Product.set_remarks(self)

    def get_details(self):
        print("%%%%%%% Product Details %%%%%%%")
        print("product_id            :{} "
              "\nproduct_name          :{} "
              "\nproduct_purchase_price:{} "
              "\nproduct_sale_price    :{} "
              "\nMargin Remarks        :{}"
              .format(self.product_id, self.product_name, self.product_purchase_price, self.product_sale_price,
                      Product.set_remarks(self)))

p = Product("oil","olive oil",2.99,4.99,"Profit")
p.get_details()
p.set_details()
p.get_details()
