def oops():
    raise IndexError("Oops!")

def oops_handler():
    try:
        oops()
    except IndexError as e:
        print("Caught an IndexError:", e)

oops_handler()
