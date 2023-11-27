# Write a Python program to access a function inside a function (Tips: use function, which returns another function)

def my_function(x):
    def return_function(y):
        return x+y
    return return_function
adder = my_function(110)
print(adder(10))