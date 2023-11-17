def my_function(a,b):
    result = a**2/b
    return int(result)

try:
    all = my_function(a=5,b=0)
except ZeroDivisionError:
    print("We found a problem")
try:
    all = my_function(a='b',b='a')
except TypeError:
    print("There is a problem")
print(all)

    
    