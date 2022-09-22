#3.1 Print the Python version to the console.
import sys
print(sys.version.split(' ')[0])
#result:  3.10.0


#4.1 Import the built-in datetime module and display the namespace of this module (sorted alphabetically) as given below.
#Tip: Use the __dict__ attribute of the datetime module.

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

import datetime
list1=[]
for i in datetime.__dict__:
    list1.append(i)

list1.sort()
print('\n'.join(list1))


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

