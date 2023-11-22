import random

def guess_number():
    secret_number = random.randint(1,10)

    guess = int(input("Guess the number between 1 and 10: "))

    if guess == secret_number:
        print('Congratulations! You guessed the correct number.')
    else:
        print(f"Sorry, the correct number was {secret_number}. Try again!")

guess_number()
