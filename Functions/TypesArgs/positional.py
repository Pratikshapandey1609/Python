'''
Positional Arguments: --

These are the most common type. Arguments are matched to parameters in the function definition based on their order or position. 
The number and order of positional arguments passed during a function call must match the function's definitio
'''

def greet(name , city):
    print(f'Welcome {name} to the {city}')

greet("Raju" , "Bangluru")