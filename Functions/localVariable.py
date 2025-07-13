'''
Local Variables:
Local variables are defined within a function or a block of code and are only accessible 
within that specific function or block.
'''

def msg():
    choice = "I love java , python !!"
    print(choice)

msg()
# print(choice) ## Accesing the local varible outside the function
''' print(choice)
          ^^^^^^
NameError: name 'choice' is not defined'''