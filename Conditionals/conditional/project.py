num_1 = float(input("Enter Number 1 = "))
num_2 = float(input("Enter Number 2 = "))

choice = input("Enter your Choice = + - * / // ** = : ")

if choice == '+':
    print(f'Addition of two number : {num_1 + num_2}')

elif choice == '-':
    print(f"Substraction of two number : {num_1 - num_2}")

elif choice == '*':
    print(f"Multiplication of two number is : {num_1 * num_2}")

elif choice == '/':
    print(f"Division of two number is : {num_1 / num_2}")

elif choice == '//':
    print(f"Floor division of two number is : {num_1 //  num_2}")

elif choice == '**':
    print(f"Exponential of two number is : {num_1 ** num_2}")

elif choice == '=':
    print(f"Equal of two number  is : {num_1 * num_2}")
    
else:
    print("wrong Operator !!")
