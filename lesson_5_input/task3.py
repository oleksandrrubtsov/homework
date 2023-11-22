import random


def random_strings(input_string, num_strings):
    characters = list(input_string)

    
    for _ in range(num_strings):
        random.shuffle(characters)
        random_string = ''.join(characters)
        print(random_string)

input_string = input("Enter a string: ")

random_strings(input_string, 5)
