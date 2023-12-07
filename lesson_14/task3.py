def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            
            if len(args) != 1:
                print("Invalid number of arguments.")
                return False

           
            if not isinstance(args[0], type_):
                print(f"Invalid argument type. Expected {type_}, got {type(args[0])}.")
                return False

            
            if len(args[0]) > max_length:
                print(f"Argument length exceeds the maximum allowed length of {max_length}.")
                return False

            
            for symbol in contains:
                if symbol not in args[0]:
                    print(f"Argument must contain '{symbol}'.")
                    return False

            
            result = func(*args, **kwargs)
            return result

        return wrapper
    return decorator

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('05years') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
