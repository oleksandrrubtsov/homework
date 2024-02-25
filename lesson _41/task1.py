

class Stack:
    def __init__(self):
        self.items = []    
    
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    
    def peek(self):
        if not self.is_empty():
            return  self.items[-1]
    
    def is_empty(self):
        return not bool (self.items)
    
    def size(self):
        return len(self.items)
    
def reverse(self,item):
    stack = Stack()

    for i in item:
        stack.push(i)

    while not  stack.is_empty():
        print(stack.pop(),end='')
item = ("We will conquere COVID-19") 
print("Item: ", item)
reverse(None,item)