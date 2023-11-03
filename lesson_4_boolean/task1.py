m = input("Write your string: ")

if len(m) < 2:
    print("")
else:
    nm = m[:2] + m[-2:]
    print(nm)
