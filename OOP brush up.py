################################Start#################################################
#3.1 Print the Python version to the console.
from doctest import Example
import sys
print(sys.version.split(' ')[0])
#result:  3.10.0
################################L#################################################

################################Namespaces#################################################
#4.1 Import the built-in datetime module and display the namespace of this module (sorted alphabetically) as given below.
#Tip: Use the __dict__ attribute of the datetime module.

import datetime
list1=[]
for i in datetime.__dict__:
    list1.append(i)

list1.sort()
print('\n'.join(list1))

# Expected result:
# MAXYEAR
# MINYEAR
# __builtins__
# __cached__
# __doc__
# __file__
# __loader__
# __name__
# __package__
# __spec__
# date
# datetime
# datetime_CAPI
# sys
# time
# timedelta
# timezone
# tzinfo


#4.3 The Product class is given below. Display the namespace (value of the __dict__ attribute) of this class as shown below.
# Given:
# import uuid

# class Product:
#     def __init__(self, product_name, price):
#         self.product_id = self.get_id()
#         self.product_name = product_name
#         self.price = price

#     def __repr__(self):
#         return (
#             f"Product(product_name='{self.product_name}', "
#             f"price={self.price})"
#         )

#     @staticmethod
#     def get_id():
#         return str(uuid.uuid4().fields[-1])[:6]
        
print('\n'.join([i for i in Product.__dict__]))

# Expected result:
# __module__
# __init__
# __repr__
# get_id
# __dict__
# __weakref__
# __doc__



#4.4 The Product class is specified. An instance of this class named product was created. Display the namespace (value of the __dict__ attribute) of this instance as shown below.

# Given:
# import uuid


# class Product:

#     def __init__(self, product_name, product_id, price):
#         self.product_name = product_name
#         self.product_id = product_id
#         self.price = price

#     def __repr__(self):
#         return (
#             f"Product(product_name='{self.product_name}', "
#             f"price={self.price})"
#         )


# product = Product('Mobile Phone', '54274', 2900)
print(product.__dict__)

# Expected result:
# {'product_name': 'Mobile Phone', 'product_id': '54274', 'price': 2900}
#################################################################################


################################LEGB#################################################
# 5.1 The stock_info() function is defined. Using the appropriate attribute of the stock_info() function, display the names of all arguments to this function to the console.

# An example of calling the function:
# def stock_info(company, country, price, currency):
#     return f'Company: {company}\nCountry: {country}\nPrice: {currency} {price}'
# print(stock_info('Apple', 'USA', 115, '$'))

print(stock_info.__code__.co_varnames)

# Expected result:
# ('company', 'country', 'price', 'currency')



#5.2 Using the builtins module import the sum() function. Then display its documentation of this function. Call the function on the list [-4, 3, 2] and print the result to the console.

from builtins import sum  
help(sum)
print(sum([-4, 3, 2]))


# 5.3 A global variable counter is given with an incorrectly implemented update_counter() function. Correct the implementation of the update_counter() function so that you can modify the counter variable from this function. Then call the update_counter() function.
# Tip: Use the global statement.


# counter = 1

# def update_counter():
    global counter
#     counter += 1
#     print(counter)
    
update_counter()



# 5.4 The following global variables are given:

# counter
# dot_counter

# and incorrectly implemented update_counters() function. Correct the implementation of the update_counters() function so that you can modify the values of the given global variables from this function. Then call update_counters() 40 times.
# In response, print the value of the counter and dot_counter global variables to the console as shown below.



# Tip: Use the global statement.

# counter = 0
# dot_counter = ''

# def update_counter():
    # global counter,dot_counter
    counter += 1
    dot_counter += '.'


[update_counter() for i in range(40)]
print(counter)
print(dot_counter)


# Expected result:
# 40
# ........................................









# 5.5 A display_info() function was implemented. This function has an incorrectly implemented internal update_counter() function. Correct the implementation of this function so that you can modify non-local variables: counter and dot_counter from the internal function update_counter().

# In response, call display_info() with the number_of_updates argument set to 10.
# Tip: Use the nonlocal statement.

# def display_info(number_of_updates=10):
#     counter = 100
#     dot_counter = ''

#     def update_counter():
          nonlocal counter,dot_counter
#         counter += 1
#         dot_counter += '.'
    
#     [update_counter() for _ in range(number_of_updates)]

#     print(counter)
#     print(dot_counter)

# display_info()



# Expected result:

# 110
# ..........
#################################################################################


################################args,kwargs#################################################
# 6.1 Implement a function called stick() that takes any number of bare arguments and return an object of type str being a concatenation of all arguments of type str passed to the function with the '#' sign (see below).

# As an answer call the stick() function in the following ways (print the result to the console):
# stick('sport', 'summer')
# stick(3, 5, 7)
# stick(False, 'time', True, 'workout', [], 'gym')

def stick(*args)->str:
    print('#'.join([i     for i in args         if  isinstance(i, str)]))

stick('sport', 'summer')
stick(3, 5, 7)
stick(False, 'time', True, 'workout', [], 'gym')


# Result  
# [IN]: stick('sport', 'summer', 4, True)
# [OUT]: 'sport#summer'


#6.2Implement a function called display_info() which prints the name of the company (as shown below) and if the user also passes an argument named price, it prints the price (as shown below).
# Example1
# [IN]: display_info(company='Apple')
# Company name: Apple

# Example2
# [IN]: display_info(company='Apple', price=114)
# Company name: Apple
# Price: $ 114

# Example 3
# display_info(company='CD Projekt', price=100)
# Expected result: 
# Company name: CD Projekt
# Price: $ 100

import json
def display_info(company, **kwargs):
    print(f'Company name: {company}')
    if kwargs != {}:
        print(json.dumps(kwargs).replace(':',': $').replace('"','').replace('{','').replace('}','').replace('p','P'))
        
display_info(company='CD Projekt', price=100)
#################################################################################











################################Classes the basics#################################################
# 7.4 Display the value of the __name__ attribute of the Vehicle class to the console.

# class Vehicle:
#     """This is a Vehicle class."""
    
print(Vehicle.__name__)


################################Classes attr#################################################
# 8.1 Implement a class named Phone. In the Phone class, define a class attribute named brand and set its value to 'Apple'. Then, using dot notation and print() function, display the value of the brand attribute of the Phone class to the console.
class Phone:
    brand = 'Apple'
    
print(Phone.brand)


# 8.2 Implement a class named Phone. In the Phone class, define two class attributes with names:
# brand
# model

# and set their values to:
# 'Apple'
# 'iPhone X'

# Find it's attr with getattr
class Phone:
    brand = 'Apple'
    model = 'iPhone X'
print(getattr(Phone,'brand'))
print(getattr(Phone,'model'))


# 8.3 A class named Phone is defined below. Using dot notation, modify the value of the attributes:
# brand to 'Samsung'
# model to 'Galaxy'

# In response, print the values for the brand and model attributes to the console as shown below.
class Phone:
    brand = 'Apple'
    model = 'iPhone X'
Phone.brand = 'Samsung'
Phone.model = 'Galaxy'

print(f'brand: {Phone.brand}')
print(f'model: {Phone.model}')


# 8.4A class named Laptop is defined below. Using the setattr() built-in function modify the value of attributes:
# brand to 'Acer'
# model to 'Predator'
# In response, using the built-in function getattr() and print(), print the values of the brand and model attributes to the console as shown below.
class Laptop:
    brand = 'Lenovo'
    model = 'ThinkPad'
setattr(Laptop, 'brand', 'Acer')
setattr(Laptop, 'model', 'Predator')
print(f"brand: {getattr(Laptop, 'brand')}")
print(f"model: {getattr(Laptop, 'model')}")


# 8.5Implement a class named OnlineShop with the class attributes set appropriately:
# sector to the value 'electronics'
# sector_code to the value 'ELE'
# is_public_company to the value False
# Then, using dot notation, add a class attribute called country and set its value to 'USA'. In response, print the user-defined OnlineShop class attribute names as shown below.
class OnlineShop:
    sector = 'electronics'
    sector_code  = 'ELE'
    is_public_company   = 'False'

OnlineShop.country = 'USA'
list1=[]
for i in OnlineShop.__dict__:
    list1.append(i)
    
    
for j in sorted(list1,reverse=True):
    if '__' in j:
        list1.remove(j)
print(list1)



