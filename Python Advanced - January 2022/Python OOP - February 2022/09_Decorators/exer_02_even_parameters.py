def even_parameters(function):
    def wrapper(*args):
        for value in args:
            if not isinstance(value,int) or not value%2==0:
                return "Please use only even numbers!"
        return function(*args)
    return wrapper


@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))