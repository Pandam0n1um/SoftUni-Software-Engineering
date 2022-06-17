def cache(func_ref):
    log={}
    def wrapper(number):
        if number in log:
            return log[number]
        result=func_ref(number)
        log[number]=result
        return result
    wrapper.log=log
    return wrapper


# TODO: Implement

@cache
def fibonacci(n):
    if n < 2:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# fibonacci(3)
# print(fibonacci.log)
# fibonacci(4)
# print(fibonacci.log)

print()
print()
print()
fibonacci(1)
print(fibonacci.log)
