"""
__init__ -----------> it's a constructor
"""

class Car:
    def __init__(self, brand , color):
        self.brand = brand
        self.color = color

car1 = Car('Tesla','Red') #values Automatically sets here
print(car1.brand, car1.color)

""" Syntax: ------------
class className:
    def __init__(self , parameter1 , parameter2):
        self.property1 = parameter1
        self.property2 = parameter2

___init__()   :--  constructor
self.property :--  store value inside the objects
        
"""


