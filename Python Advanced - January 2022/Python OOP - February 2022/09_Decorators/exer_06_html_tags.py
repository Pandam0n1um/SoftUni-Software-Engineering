def tags(tag_name):
    def decorator(func_ref):
        def wrapper(*args):
            result=func_ref(*args)
            return f"<{tag_name}>{result}</{tag_name}>"
        return wrapper
    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))
@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))
