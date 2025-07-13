try:
    num1 = int(input('Enter first  number :--'))
    num2 = int(input('Enter second number : --- '))

    try:
        result = num1 / num2
        print(f'Result : {result}')
    except ZeroDivisionError:
        print("you cannot devide with zero")
except ValueError:
    print("you must provide a valid input")