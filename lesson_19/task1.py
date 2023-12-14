import itertools
import random

def with_index (iterable, start = 0):
    for index, item in enumerate(iterable, start):
        print(f"{index}: {item}") 

list_to_print = ["A", "B", "C"]
char_list_to_print = ['a', 'b', 'c']

with_index(list_to_print)
with_index(char_list_to_print, start=1)