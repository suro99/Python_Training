#---- __repr__

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
       
    def __repr__(self):
        return f"Person('{self.name}',{self.age})"
   
p = Person("Viren", 34)
print(repr(p))    # syntax
print(p)

#---- __str__
 
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
       
    def __str__(self):
        return f"{self.name}', age is {self.age}"
   
p = Person("Viren", 34)
print(str(p))    # syntax
print(p)
 
p1 = Person('Ravi', 45)
print(p1)