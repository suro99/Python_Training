class Bird:
    def fly(self):
        print("Bird can fly ")
       
class Aeroplane:
    def fly(self):
        print("Aeroplane can fly ")
       
class Fish:
    def swim(self):
        print("Fish can swim  ")
       
def let_it_fly(flyer):
    flyer.fly()
 
let_it_fly(Bird())
let_it_fly(Aeroplane())
let_it_fly(Fish())       # attributeError