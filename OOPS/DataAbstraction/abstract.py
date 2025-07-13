from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass # no implementation

class Car(Vehicle):
    def start(self):
       # return super().start()
       print('Car start with a key')

class Bike(Vehicle):
    def start(self):
        #return super().start()
        print('Bike starts with a Button')

car = Car()
bike = Bike()

car.start()
bike.start()