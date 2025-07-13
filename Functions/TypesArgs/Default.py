'''
Default Arguments : 
Parameters can be assigned default values in the function definition. 
If an argument for that parameter is not provided during the function call, 
the default value is used.
'''

def greet(name = "Guest" , city = 'Mumbai'):
    print(f'hello {name} to the city {city}') 

greet("Bob"  , "pune")
greet()
