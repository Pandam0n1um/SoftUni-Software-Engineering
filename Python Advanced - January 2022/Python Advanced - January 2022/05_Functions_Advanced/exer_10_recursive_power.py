def recursive_power(base, exponent):
    if exponent==1:
        return base
    return base*recursive_power(base,exponent-1)


print(recursive_power(2, 10))
print(recursive_power(10, 100))
