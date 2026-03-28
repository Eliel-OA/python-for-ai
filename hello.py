
class Animal:
  def __init__(self, name):
    self.name = name
    
  def eat(self):
    return f"{self.name} is eating"
  
  def sleep(self):
    return f"{self.name} is sleeping"
  
  
  
class Dog(Animal):
  
  def bark(self):
    return f"{self.name} says woof"
  

my_dog = Dog("Max")

my_dog2 = Dog("Jerem")

my_dog.bark()
my_dog.eat()
my_dog.sleep()
  