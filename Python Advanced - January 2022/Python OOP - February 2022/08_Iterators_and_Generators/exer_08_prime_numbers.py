from math import sqrt
# def is_prime(number):
# 	if number <= 1:
# 		return False
# 	if number == 2:
# 		return True
# 	for i in range(2, number):
# 		if number % i == 0:
# 			return False
# 	return True
#
#
# def get_primes(numbers):
# 	for number in numbers:
# 		if is_prime(number):
# 			yield number

def is_prime(number):
	if number <= 1:
		return False
	if number == 2:
		return True
	if number == 2:
		return True
	for i in range(3, (number//2),2):
		if number % i == 0:
			return False
	return True


def get_primes(numbers):
	for number in numbers:
		if is_prime(number):
			yield number


print(list(get_primes([2*(10**999999), 4, 3, 5, 6, 9, 1, 0])))
