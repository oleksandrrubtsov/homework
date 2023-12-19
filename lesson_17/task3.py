class Fraction:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Fraction(self.x + other.x, self.y + other.y)
    
    def __sub__(self,other):
        return Fraction(self.x - other.x, self.y - other.y)
    
    def __mul__(self,other):
        return Fraction(self.x * other.x, self.y * other.y)
    
    def __truediv__(self,other):
        return Fraction(self.x / other.x, self.y / other.y)

    def __eq__(self,other):
        if isinstance(other,Fraction):
            return self.x == other.x and self.y == other.y
        else:
            return False
        
             

p1 = Fraction(1, 2)
p2 = Fraction(3, 4)

p3 = p1 + p2  
p4 = p2 - p1  

print(p3.x, p3.y)  
print(p4.x, p4.y)
