number = input("What is your phone number?: ")

if len(number) == 10:
    print("Your number is valid")
elif len(number) > 10:
    print("Your number is too long")
elif number.isdigit:
    print("Your phone number must contains only numbers")
else:
    print("Not required characters found")