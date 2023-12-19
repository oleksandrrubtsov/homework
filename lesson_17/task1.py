class Animal:
    def talk(self):
        pass



class Dog(Animal):
    def talk(self):
        return 'Woof'

class Cat(Animal):
    def talk(self):
        return 'Meow'
    
dog = Dog()
cat = Cat()

print(dog.talk())  
print(cat.talk())