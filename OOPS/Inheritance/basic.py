class Animal:
    def speak(self):
        print('Animal make sounds !')

class Dog(Animal):
    def bark(self):
        print('Dogs bark')

dog = Dog()
dog.bark()
dog.speak()

animal = Animal()
animal.speak()


