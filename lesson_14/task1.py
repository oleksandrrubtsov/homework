




def function_1(func):
    def wrapper (*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)
    return wrapper



@ function_1
def example_1(arg1, arg2, kwarg1 = None):
    print(example_1.__name__)

example_1("Hello", arg2="World", kwarg1="GPT")




