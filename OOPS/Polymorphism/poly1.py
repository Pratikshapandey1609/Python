# polymorphism with classes

class Bird():
    def sound(self):
        print("Birds make sounds!!")

class Crow(Bird):
    def sound(self):
        print('Crow sya "caw caw')
        #return super().sound() Birds make sounds!!

class Parrot(Bird):
    def sound(self):
        print('Parrot sounds , squak !!')
        #return super().sound() #Birds make sounds!!


bird1 = Crow()
bird2 = Parrot()

bird1.sound()
bird2.sound()