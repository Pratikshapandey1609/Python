def my_decorator(func):
    def wrapper():
        print("Something is happing before the function is called ")
        func()
        print("Something is happing after the function is called")
    return wrapper

@my_decorator
def say_hello():
    print("hello")    

say_hello()