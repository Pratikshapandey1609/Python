'''
Exit a function and go back to the function where it call 
'''

def get_full_name(first_name , lat_name):
    '''return the full name '''
    full_name = f'{first_name} {lat_name}'
    return full_name

name = get_full_name("prisha" , "Mishra")
print(name)