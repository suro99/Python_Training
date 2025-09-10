class Animal:
    def speak(self):
        print("The animal is making noise")
       
class Dog(Animal):
    def speak(self):
        print("The dog is making noise")
       
class Cat(Animal):
    def speak(self):
        print("The cat is making noise")
       
def mak_animal_speak(animal):
    animal.speak()
   
animals = [Dog(), Cat(), Animal()]
for a in animals:
    mak_animal_speak(a)