"""
1. Клас для обчислення площі прямокутника:
Створіть клас Rectangle, який має атрибути для зберігання довжини та ширини прямокутника. Використовуйте декоратор @property для повернення площі прямокутника.
"""
class Rectangle:
   def __init__(self, length, width):
      self.length = length
      self.width = width

   @property
   def area(self):
      return self.length * self.width 
   
rectangle = Rectangle (length=5, width=3)

print("Довжина:", rectangle.length)
print("Ширина:", rectangle.width)
print("Площа:", rectangle.area)


