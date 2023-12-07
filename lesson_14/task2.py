import functools
# Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
def stop_words(words:list):
    def decor (func):
        @functools.wraps (func)
        def wrapper (*args, **kwargs):
            result = func (*args, **kwargs)
            if isinstance(result,str):
                result = ''.join(['*' if word in words else word for word in result.split()])
            return result
        return wrapper
    return decor

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    print( f"{name} drinks pepsi in his brand new BMW!")


print(create_slogan("Alex"))
    





