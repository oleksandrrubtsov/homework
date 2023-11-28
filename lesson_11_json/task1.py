str1 = input('Your info: ')
with open("lesson_11_json/myfile.txt", "w") as writer:
    writer.write(str1)