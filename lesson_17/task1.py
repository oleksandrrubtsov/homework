def animals_say_hello(animal):
   print(animal.say_hi())

class Animal:
   def say_hi():
      pass

class Cat(Animal):
   def say_hi(self):
      return 'Meow!'
   
class Dog(Animal):
   def say_hi(self):
      return 'Woof!'
      
cat = Cat()
dog = Dog()

animals_say_hello(cat)
animals_say_hello(dog)

