"""
in - True / False
not in -  opposite of in
"""

lst_1 = [1,2,3,4,5,6]

check = int(input("Enter a number to check : = "))

# if check in lst_1:
#     print("Found !!")
# else:
#     print("Not Found !!")

if check not in lst_1:
    print("No number is  Not Found !!")
else:
    print("yes Found !!")


