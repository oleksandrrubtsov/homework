"""
Create your own implementation of a built-in function range, named in_range(), which takes three parameters: 'start', 'end', and optional step. Tips: See the documentation for 'range' function
"""


def in_range (start, end, step = 1):
    result = []

    if step == 0:
        raise ValueError
        
    if step > 0:
        current_value = start
        while current_value < end:
            result.append(current_value)
            current_value += step

    elif step < 0:
        current_value = start
        while current_value > end:
            result.append(current_value)
            current_value += step

    return result
    
print(in_range(1, 10, 2))
print(in_range(10, 1, -2))
print(in_range(0, 10))



