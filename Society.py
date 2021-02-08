'''
#############################################################################################
#*******************************************************************************************#
#           Copyright (c) 2020 pyCoder|semih Corporation;) All rights reserved.            ##
#                                   [Timestamp:20210207]                                   ##
#*******************************************************************************************#
#############################################################################################
'''
# Question 1:
# Create the class Society with following information:
# society_name, house_no, no_of_members, flat, income.
# Methods :
# An __init__ method to assign initial values of society_name, flat, house_no, no_of_members, income
# input_data() To read information from members
# allocate_flat() To allocate flat according to income using the below table.
# show_data() to display the details of the entire class.
# Income	            Flat
# >=25000	            A Type
# >=20000 and <25000	B Type
# >=15000 and <20000	C Type
# <15000	            D Type

class Society:
    def __init__(self, society_name, house_no, no_of_members, flat, income):
        self.society_name = society_name
        self.house_no = house_no
        self.no_of_members = no_of_members
        self.flat = flat
        self.income = income

    @classmethod
    def input_data(cls, data):
        society_name, house_no, no_of_members, flat, income = data.split(",")

        return cls(society_name, house_no, no_of_members, flat, int(income))

    def assignate_flat(self):
        if self.income >= 25000:
            return "A Type"
        elif 20000 <= self.income < 25000:
            return "B Type"
        elif 15000 <= self.income < 20000:
            return "C Type"
        elif self.income < 15000:
            return "D Type"

    def show_data(self):
        print("%%%%%% information %%%%%%")
        print("Society_name  : {} "
              "\nHouse_no      : {} "
              "\nNo_of_members : {} "
              "\nFlat          : {} "
              "\nIncome        : {}"
              .format(self.society_name, self.house_no, self.no_of_members, Society.assignate_flat(self), self.income))

data1 = "farmer,111,1,1,10000"
data2 = "teacher,222,2,2,20000"
data3 = "doctor,333,3,3,30000"

uye1 = Society.input_data(data1)
uye2 = Society.input_data(data2)
uye3 = Society.input_data(data3)

print(uye1.show_data())
print(uye2.show_data())
print(uye3.show_data())

'''Asagidaki 3 satiri; istenen format belki asagidaki yontemle input gondermektir, diye ekledim.'''

# data0 = input("enter a data (society_name, house_no, no_of_members, flat, income):")
# uye0 = Society.input_data(data0)
# print(uye0.show_data())
