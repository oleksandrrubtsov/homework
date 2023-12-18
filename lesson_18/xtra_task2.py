"""
2. Створіть дескриптор DiscountLimit, який визначає максимальний обсяг знижки для товару. Забороніть встановлення знижки більше, ніж встановлено за лімітом.
"""

class DiscountLimit:
    def __init__(self, limit):
        self._limit = limit

    def __get__(self, instance, owner):
        return getattr(instance, '_discount', 0)

    def __set__(self, instance, value):
        if value > self._limit:
            raise ValueError(f"Знижка не може бути більше, ніж {self._limit}%")
        setattr(instance, '_discount', value)

    def __delete__(self, instance):
        delattr(instance, '_discount')


class Product:
    discount = DiscountLimit(limit=20)  

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self._discount = 0



product1 = Product(name="Лаптоп", price=1000)


product1.discount = 15
print(f"{product1.name}: Ціна зі знижкою {product1.discount}%: ${product1.price * (1 - product1.discount / 100)}")


