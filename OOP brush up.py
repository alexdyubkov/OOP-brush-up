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





# 8.6  A class named OnlineShop was defined with the class attributes set accordingly:
# sector to the value 'electronics'
# sector_code to the value 'ELE'
# is_public_company to the value False
# Using the del statement remove the class attribute named sector_code. In response, print the rest of the user-defined OnlineShop class attribute names as a list as shown below.

# class OnlineShop:
#     sector = 'electronics'
#     sector_code = 'ELE'
#     is_public_company = False


del OnlineShop.sector_code

list1=[]
for i in OnlineShop.__dict__:
    if not i.startswith('_'):
        list1.append(i)
print(list1)






#8.7 same as 6.6 but with delattr() 
# class OnlineShop:
#     sector = 'electronics'
#     sector_code = 'ELE'
#     is_public_company = False

delattr(OnlineShop,'sector_code')

list1=[]
for i in OnlineShop.__dict__:
    if not i.startswith('_'):
        list1.append(i)
print(list1)



# 8.8A class named OnlineShop was defined with the class attributes set accordingly:
# sector to the value 'electronics'
# sector_code to the value 'ELE'
# is_public_company to the value False
# Display all user-defined OnlineShop class attribute names with their values as shown below.
# sector -> electronics
# sector_code -> ELE
# is_public_company -> False


# class OnlineShop:
#     sector = 'electronics'
#     sector_code = 'ELE'
#     is_public_company = False
 
 
for attr, value in OnlineShop.__dict__.items():
    if not attr.startswith('_'):
        print(f'{attr} -> {value}')






        
 # 9.1 Implement a class called Laptop that sets the following instance attributes when creating an instance:
# brand
# model
# price

# Then create an instance named laptop with the following attribute values:
# brand = 'Acer'
# model = 'Predator'
# price = 5490

# Tip: Use the special method __init__().
# In response, print the value of the __dict__ attribute of the laptop instance.

#result
#{'brand': 'Acer', 'model': 'Predator', 'price': 5490}

class Laptop:
    def __init__(self, brand, model , price):
        self.brand=brand
        self.model=model
        self.price=price
        
laptop=Laptop(brand = 'Acer',model = 'Predator',price = 5490)

print(laptop.__dict__)


# 9.2 A class called Laptop was implemented.
# Implement a method in the Laptop class called display_instance_attrs() that displays the names of all the attributes of the Laptop instance.
# Then create an instance named laptop with the given attribute values:
# brand = 'Dell'
# model = 'Inspiron'
# price = 3699

# In response, call display_instance_attrs() method on the laptop instance.
# Expected result:
# brand
# model
# price

class Laptop:
    def __init__(self, brand, model , price):
        self.brand=brand
        self.model=model
        self.price=price
    def display_instance_attrs(self):
        for i in self.__dict__: 
            print(i)
    
        
laptop=Laptop(brand = 'Dell',model = 'Inspiration',price = 3699)

laptop.display_instance_attrs()


#9.3A class called Laptop was implemented.

# Implement a method in the Laptop class called display_attrs_with_values(), which displays the names of all the attributes of the Laptop class with their values as shown below (attribute name -> attribute value).
# Then create an instance named laptop with the following values:

# brand = 'Dell'
# model = 'Inspiron'
# price = 3699

# In response, call display_attrs_with_values() method on the laptop instance.
# Expected result:
# brand -> Dell
# model -> Inspiron
# price -> 3699


class Laptop:
    def __init__(self, brand, model , price):
        self.brand=brand
        self.model=model
        self.price=price
    def display_attrs_with_values(self):
        for i,j in self.__dict__.items():
            print(i,' ->',j)
    
        
laptop=Laptop(brand = 'Dell',model = 'Inspiration',price = 3699)

laptop.display_attrs_with_values()



#9.4Implement a class named Vector that takes any number of n-dimensional vector coordinates as arguments when creating an instance (without any validation) and assign to instance attribute named components. Then create two instances with following coordinates:
# (1, 2)
# (4, 5, 2)
# and assign to variables v1 and v2 respectively.

# In response, print the value of the components attribute for v1 and v2 instance as shown below.
# Expected result:
# v1 -> (1, 2)
# v2 -> (4, 5, 2)

class Vector:
    def __init__(self, *components):
        self.components = components
v1 = Vector(1, 2)
v2 = Vector(4, 5, 2)

print(f'v1 -> {v1.components}')
print(f'v2 -> {v2.components}')


#9.5 Implement a class called Bucket that takes any number of named arguments (keyword arguments - use **kwargs) when creating an instance. The name of the argument is the name of the instance attribute, and the value for the argument is the value for the instance attribute.
# Example:
# [IN]: bucket = Bucket(apple=3.5)
# [IN]: print(bucket.__dict__)
# [OUT]: {'apple': 3.5}


# Then create instance named bucket by adding the following attributes with their values:
# apple = 3.5
# milk = 2.5
# juice = 4.9
# water = 2.5

# In response, print the value of __dict__ attribute for the bucket instance.

# Expected result:
# {'apple': 3.5, 'milk': 2.5, 'juice': 4.9, 'water': 2.5}

class Bucket:
    def __init__(self, **kwargs):
        # for attr_name, attr_value in kwargs.items():
        #     print(self.attr_name, self.attr_value)
        self.kwargs=kwargs

bucket=Bucket(
    apple = 3.5,
    milk = 2.5,
    juice = 4.9,
    water = 2.5)

print(next(iter(bucket.__dict__.values())))

# 9.6 Implement a class called Car that sets the following instance attributes when creating an instance:
# brand
# model
# price
# type_of_car, by default 'sedan'

# Then create an instance named car with the given values:
# brand = 'Opel'
# model = 'Insignia'
# price = 115000

# In response, print the value of the __dict__ attribute of the car instance.

# Expected result:
# {'brand': 'Opel', 'model': 'Insignia', 'price': 115000, 'type_of_car': 'sedan'}

class Car:
    def __init__(self, brand,model, price, type_of_car='sedan'):
        self.brand = brand 
        self.model = model
        self.price = price
        self.type_of_car = type_of_car   

car=Car(brand='Opel', model='Insignia', price = 115000)

print(car.__dict__)


#9.7Implement a class called Laptop that sets the following instance attributes when creating an instance:
# brand
# model
# price
# When creating an instance, add validation for the price attribute. The value of the price attribute must be an int or float type greater than zero. If it is not, raise the TypeError with the following message:
# 'The price attribute must be a positive int or float.'


# Then create an instance called laptop with the given attributes:
# brand = 'Acer'
# model = 'Predator'
# price = 5490
# In response, print the value of the __dict__ attribute of the laptop instance.

# Expected result:
# {'brand': 'Acer', 'model': 'Predator', 'price': 5490}


class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        if isinstance(price, (int, float)) and price > 0:
            self.price = price
        else:
            raise TypeError(
                'The price attribute must be a positive int or float.'
            )

laptop = Laptop('Acer', 'Predator', 5490)
print(laptop.__dict__)
       

#10.1 Implement a class called Laptop that sets the following instance attributes when creating an instance:
#brand as a bare instance attribute
#model as a protected attribute
#price as a private attribute
#Then create an instance named laptop with the following arguments:
# 'Acer'
# 'Predator'
# 5490
# In response, print the value of the __dict__ attribute of the laptop instance.

#Results
# {'brand': 'Acer', '_model': 'Predator', '_Laptop__price': 5490}

class Laptop:
    def __init__(self,brand, model, price):
        self.brand=brand
        self._model=model
        self.__price=price

laptop=Laptop(brand='Acer', model='Predator', price=5490)

print(laptop.__dict__)


#10.2A class called Laptop was implemented. Then, an instance of the Laptop class named laptop was created with the following arguments:
# 'Acer'
# 'Predator'
# 5490
# In response, print the value for each instance attribute (on a separate line) of the laptop instance as shown below.
# brand -> Acer
# model -> Predator
# price -> 5490

class Laptop:
    def __init__(self,brand, model, price):
        self.brand=brand
        self._model=model
        self.__price=price

laptop=Laptop(brand='Acer', model='Predator', price=5490)

# print(laptop.__dict__)

res=[]
for i,j in laptop.__dict__.items():
    res.append(str(i)+' -> '+str(j))

for i in res:
    i=i.replace('_','').replace('Laptop','')
    print(i)


#or
class Laptop:

    def __init__(self, brand, model, price):
        self.brand = brand
        self._model = model
        self.__price = price


laptop = Laptop('Acer', 'Predator', 5490)
print(f'brand -> {laptop.brand}')
print(f'model -> {laptop._model}')
print(f'price -> {laptop._Laptop__price}')






#10.3An implementation of the Laptop class is given. Implement a method in the Laptop class called display_private_attrs() that displays the names of all private attributes of the instance. Then create an instance with the given arguments:
# 'Acer'
# 'Predator'
# 'AC-100'
# 5490
# 0.2
# and assign it to the variable laptop. In response, call display_private_attrs() on the laptop instance.

# Expected result:
# _Laptop__price
# _Laptop__margin


class Laptop:

    def __init__(self, brand, model, code, price, margin):
        self.brand = brand
        self._model = model
        self._code = code
        self.__price = price
        self.__margin = margin
    
    def display_private_attrs(self):
        for i in laptop.__dict__.keys():
            if '__' in i:
                print(i)

laptop = Laptop('Acer','Predator','AC-100', 5400, 0.2)
laptop.display_private_attrs()








#10.4An implementation of the Laptop class is given. Implement a method called display_protected_attrs() in the Laptop class that displays the names of the protected attribute of the instance. Then create an instance with the given arguments:
# 'Acer'
# 'Predator'
# 'AC-100'
# 5490
# 0.2
# and assign it to the variable laptop. In response, call display_protected_attrs() on the laptop instance.

# Expected result:
# _model
# _code

class Laptop:

    def __init__(self, brand, model, code, price, margin):
        self.brand = brand
        self._model = model
        self._code = code
        self.__price = price
        self.__margin = margin
    
    def display_private_attrs(self):
        for i in laptop.__dict__.keys():
            if '_'  in i and not  '__' in i:
                print(i)


laptop = Laptop('Acer','Predator','AC-100', 5400, 0.2)

laptop.display_private_attrs()




#12.1 Implement a class called Laptop which in the __init __() method sets the value of the price protected attribute that stores the price of the laptop (without any validation). Then implement a method to read that attribute named get_price() and a method to modify that attribute named set_price() without validation as well.
#Then create an instance of the Laptop class with a price of 3499 and follow these steps:
#using the get_price() method print the value of the price protected attribute to the console
#using the set_price() method, set the value of the price protected attribute to 3999
#using the get_price() method print the value of the price protected attribute to the console

#Expected result:
#3499
#3999

class Laptop:
    def __init__(self, price):
        self._price = price
    def get_price(self):
        return self._price
    def set_price(self, value):
        self._price = value
laptop = Laptop(3499)
print(laptop.get_price())
laptop.set_price(3999)
print(laptop.get_price())




#12.2 A class called Laptop was implemented. Implement a method named set_price() to modify price attribute that validates the value. Validation checks:
# whether the value is an int or float type, if it is not raise a TypeError with the following message:
# 'The price attribute must be an int or float type.'
# whether the value is positive, if it is not raise ValueError with the following message:
# 'The price attribute must be a positive int or float value.'
# Then create an instance of the Laptop class with a price of 3499 and try to set '-3000' to the price using set_price() method. If an error is raised, print the error message to the console. Use a try ... except ... clause in your solution.


# Expected result:
# The price attribute must be an int or float type.

class Laptop:
    def __init__(self, price):
        self._price = price
    def get_price(self):
        return self._price
    def set_price(self, value):
        if isinstance(value, int or float):
            if value > 0:
                self._price = value
            else:
                raise ValueError('The price attribute must be a positive int or float value.')
        else:
            raise TypeError('The price attribute must be an int or float type.')

laptop = Laptop(3499)

try:
    laptop.set_price('-3000')
except TypeError as error:
    print(error)



#12.3 A class called Laptop was implemented. The __init __() method sets the value of the price protected attribute that stores the price of the laptop (without any validation).
#Create an instance of the Laptop class with a price of 3499 and try to set the price to -3000 using the set_price() method. If an error is raised, print the error message to the console. Use a try ... except ... clause in your solution.

#Expected result:
#The price attribute must be a positive int or float value.

class Laptop:  
    def __init__(self, price):
        self._price = price
    def get_price(self):
        return self._price
    def set_price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(
                'The price attribute must be an int or float type.'
            )
        if not value > 0:
            raise ValueError(
                'The price attribute must be a positive int or '
                'float value.'
            )
        self._price = value

laptop=Laptop(3499)
try:
    laptop.set_price(-3000)
except(ValueError) as error:
    print(error)

#12.4A class called Laptop was implemented.
# Add validation of the price attribute also at the stage of creating the instance (in __init__() method).
# Then try to create an instance of the Laptop class with a price of -3499. If an error is raised, print the error message to the console. Use a try ... except ... clause in your solution.

# Expected result:
# The price attribute must be a positive int or float value.
class Laptop:
    def __init__(self, price):
        if price < 0:
            raise ValueError(
                'The price attribute must be a positive int or '
                'float value.')            
        else:
            self._price = price

    def get_price(self):
        return self._price

    def set_price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(
                'The price attribute must be an int or float type.'
            )
        if not value > 0:
            raise ValueError(
                'The price attribute must be a positive int or '
                'float value.'
            )
        self._price = value

try:
    laptop=Laptop(-3499)
except ValueError as error:
    print(error)

#12.5Implement a class named Person that has one protected instance attribute named first_name. Next, implement a method get_first_name() which reads the value of the first_name protected attribute. Then, using the get_first_name() method and the property class (do it in the standard way) create a property named first_name (read-only property).
#Create an instance of the Person class and set the first_name attribute to 'John'. Print the value of the first_name attribute of this instance to the console.
# Expected result:
# John

class Person:
    def __init__(self,first_name):
        self._first_name = first_name
    def get_first_name(self):
        return self._first_name
    name_property = property(get_first_name)

person =Person(first_name='John')
person.name_property


#12.4Implement a class named Person that has one protected attribute first_name. Next, implement a method get_first_name() which reads the value of the first_name protected attribute. Declare a method  set_first_name() that allows you to modify the value of the first_name protected attribute (without validation).
# Then, using the get_first_name(), set_first_name() methods and the property class (do it in the standard way) create a property called first_name (property to read and modify).
# Create an instance of the Person class and set the first_name attribute to 'John'. Then, using the set_first_name() method, set new value 'Mike'.
# In response, print the value of the first_name attribute to the console.

# Expected result:
# Mike

class Person:
    def __init__(self,first_name):
        self._first_name = first_name  
    def get_first_name(self):
        return self._first_name
    def set_first_name(self,first_name):
        self._first_name = first_name
    first_name = property(get_first_name,set_first_name)


person=Person('John')
person.set_first_name('Mike')
person.first_name


# 12.5Implement a class named Person that has two protected attributes: first_name and last_name, respectively. Next implement methods named get_first_name(), set_first_name(), get_last_name(), set_last_name(), which allows you to read and modify the value of the first_name and last_name protected attributes.
# Then, using the methods get_first_name(), set_first_name(), get_last_name(), set_last_name() and the property class (do it in the standard way) create properties: first_name and last_name (properties to read and modify).

# Create an instance of the Person class with the following values:
# first_name = 'John'
# last_name = 'Dow'
# Then print the values of these attributes to the console as shown below.
# Using the dot notation, modify the attribute values for this instance, respectively:
# first_name to the value 'Tom'
# last_name to the value 'Smith'
# In response, print the __dict__ attribute of the created instance to the console.

# Expected result:
# John
# Dow
# {'_first_name': 'Tom', '_last_name': 'Smith'}

class Person:
    def __init__(self,first_name,last_name):
        self._first_name = first_name  
        self._last_name = last_name
    def get_first_name(self):
        return self._first_name
    def set_first_name(self,first_name):
        self._first_name = first_name
    first_name = property(get_first_name,set_first_name)

    def get_last_name(self):
        return self._last_name
    def set_last_name(self,last_name):
        self._last_name = last_name
    last_name = property(get_last_name,set_last_name)


person=Person('John','Dow')
print(person.first_name)
print(person.last_name)

person.first_name='Tom'
person.last_name="Smith"
print(person.__dict__)


#12.6A class named Person was implemented.
# Implement the del_first_name() method to remove the first_name protected attribute.
# Then, using the methods get_first_name(), set_first_name(), del_first_name() and the property class (do this in the standard way) create property named first_name (properties to read, modify and delete).
# Create an instance of the Person class named person and assign the value 'Tom' to first_name. Use the del_first_name() method to delete the first_name attribute of the person instance. Display the __dict__ attribute of the person instance to the console.

# Expected result:
# {}

class Person:
    def __init__(self, first_name):
        self._first_name = first_name

    def get_first_name(self):
        return self._first_name
    def set_first_name(self, value):
        self._first_name = value
    def del_first_name(self, value):
        del self._first_name

    first_name=property(get_first_name, set_first_name, del_first_name)

person=Person('Tom')
person.del_first_name('Tom')
print(person.__dict__)

# 12.7 Implement a class named Pet that has one protected instance attribute name. Then implement a method name() which reads the value of the protected name attribute.
# Create a property name (read-only) using the @property decorator.
# Create an instance of the Pet class named pet and set name attribute to 'Max'. In response, print the contents of the __dict__ attribute of this instance.

# Expected result:
# {'_name': 'Max'}

class Pet:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        return self._name

pet=Pet('Max')
print(pet.__dict__)



#12.8Implement a class named Pet that has one protected instance attribute name. Then, using the @property decorator, create a property name (property to read and modify, without validation).
# Create an instance of the Pet class named pet and set the name attribute to 'Max'. Then, using dot notation, modify the value of the name attribute to 'Oscar'.
# In response, print the contents of the __dict__ attribute of this instance to the console.

# Expected result:
# {'_name': 'Oscar'}


class Pet:
    def __init__(self, name):
        self._name = name      
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,new_name):
        self._name = new_name   

pet=Pet('Max')
pet.name='Oscar'
print(pet.__dict__)


#12.9Implement a class named Pet that has two protected instance attributes: name and age, respectively. Then, using the @property decorator, create properties: name and age, respectively (properties to read and modify, without validation).
# Create an instance of the Pet class with the name pet and attributes:
# name = 'Max'
# age = 5
# Print the __dict__ attribute of the pet instance to the console. Then modify the attributes using the dot notation:
# name to the value 'Tom'
# age to the value 8
# Again, print the __dict__ attribute of the pet instance to the console again.

# Expected result:
# {'_name': 'Max', '_age': 5}
# {'_name': 'Tom', '_age': 8}

class Pet:
    def __init__(self, name, age):
        self._name = name      
        self._age = age
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,new_name):
        self._name = new_name 

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,new_age):
        self._age = new_age  



pet=Pet('Max',5)
print(pet.__dict__)
pet.name='Tom'; pet.age=8
print(pet.__dict__)

#12.10 A class called Pet is implemented that has two properties: name and age (see below). Add validation to the age property at the stage of object creation and attribute modification:
# the value of the age attribute must be an int type, otherwise raise a TypeError with the following message:
# 'The value of age must be of type int.'
# the value of the age attribute must be positive, otherwise raise ValueError with the following message:
# 'The value of age must be a positive integer.'
# Then try to create an instance of the Pet class named pet and set the following values:
# 'Max'
# 'seven'
# If there is an error, print an error message to the console. Use a try ... except ... clause in your solution.

# Expected result:
# The value of age must be of type int.
class Pet:

    def __init__(self, name, age):
        self._name = name
        self.age = age
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError(
                'The value of age must be of type int.'
            )
        if not value > 0:
            raise ValueError(
                'The value of age must be a positive integer.'
            )
        self._age = value

try:
    pet = Pet('Max', 'seven')
except TypeError as error:
    print(error)
except ValueError as error:
    print(error)

# 12.11Implement a class Game that has a property named level (read and modify property, defaults to 0). The value of the level attribute should be an integer in the range [0, 100]. Add validation at the instance creation and attribute modification stage. If the value is not of the int type, raise a TypeError with the following message:
# 'The value of level must be of type int.'
# If the value is outside the range [0, 100], set the exceeded boundary value (0 or 100 respectively). Then create a list called games consisting of four instances of the Game class:
# games = [Game(), Game(10), Game(-10), Game(120)]
# Iterate through the games list and print the value of the level attribute for each instance.

# Expected result:
# 0
# 10
# 0
# 100
class Game:
    def __init__(self, level=None):
        self.level = level if level else 0

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        if not isinstance(value, int):
            raise TypeError('The value of level must be of type int.')
        if value < 0:
            self._level = 0
        elif value > 100:
            self._level = 100
        else:
            self._level = value

games = [Game(), Game(10), Game(-10), Game(120)]
for game in games:
    print(game.level)

 

#13.1Implement a class named Circle that will have the protected instance attribute radius - the radius of the circle (readable and modifiable property). Use the @property decorator.
# Then create an instance named circle with radius=3.
# In response, display the __dict__ attribute of circle instance.

# Expected result:
# {'_radius': 3}

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(radius, new_radius):
        self._radius = new_radius

circle=Circle(radius=3)
print(circle.__dict__ )


# 13.2A class named Circle is given. Add a property called area (read-only) to the class that calculates the area of a circle with a given radius. This property should only be computed at first reading or after modifying the radius attribute. To do this, also modify the way of setting the value of the radius attribute in the __init __() method. Make sure that the value of the area attribute is recalculated after changing the radius attribute.
# Then create an instance named circle with radius=3.
# In response, display the value of the area attribute to the console (round the result to four decimal places).

# Expected result:
# 28.2743

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self._area = None
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, value):
        self._radius = value
        self._area = None
    @property
    def area(self):
        if self._area is None:
            self._area = math.pi * self._radius * self._radius
        return self._area

circle = Circle(3)
print(f'{circle.area:.4f}')

#13.3Implement a class named Rectangle which will have the following properties:
# width
# height
# The width and height of the rectangle, respectively (for reading and for modification). Also add a property named area that stores the area of the rectangle (read-only). This property should be computed only at the first reading or after modifying any of the rectangle sides. Skip attribute validation.
# Then create an instance named rectangle with a width = 3 and a height = 4 and print the information about the rectangle instance to the console as shown below.

# Expected result:
# width: 3, height: 4 -> area: 12

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._area = None

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value
        self._area = None

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
        self._area = None

    @property
    def area(self):
        if self._area is None:
            self._area = self._width * self._height
        return self._area

rectangle = Rectangle(3, 4)
print(
    f'width: {rectangle.width}, height: {rectangle.height} -> '
    f'area: {rectangle.area}'
)
    

    
    
    
    
    
  #14.1Using the classmethod class (do it in the standard way) implement a class named Person that has a class method named show_details() which displays the following text to the console:
# 'Running from Person class.'
# Try to pass the class name using the appropriate attribute of the Person class.
# In response, call the show_details() class method.

# Expected result:
# Running from Person class.

class Person:
    def show_details(cls):
        print(f'Running from {cls.__name__} class.')
        
    show_details = classmethod(show_details)

Person.show_details()

#14.2 Same as 14.1 but with decorator
class Container:
    @classmethod
    def show_details(cls):
        print(f'Running from {cls.__name__} class.')
        
Container.show_details()


# 14.3Implement a class named Person which has a class attribute named instances as an empty list. Then, each time you create an instance of the Person class, add it to the Person.instances list (use the __init __() method for this).
# Also implement a class method called count_instances() that returns the number of Person objects created (the number of items in the Person.instances list).
# Create three instances of the Person class. Then call the count_instances() class method and print result to the console

# Expected result:
# 3

class Person:
    instances = []

    def __init__(self):
        Person.instances.append(self)
    
    @classmethod
    def count_instances(cls):
        return (Person.instances)

p1 = Person()
p2 = Person()
p3 = Person()
print(Person.count_instances())
