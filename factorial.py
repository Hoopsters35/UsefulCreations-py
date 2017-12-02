import math
def get_factorial(n):
	assert n >= 0
	if n == 1 or n == 0:
		return 1
	return n * get_factorial(n-1)

def get_n(x, num):
	"""given value of x and a value you must be greater than, give n for x^n/n! > 1/num"""
	n = 1
	while (x**n / get_factorial(n)) > 1/num:
		n += 1
	return n

def get_2n_1(x, num):
	"""given value of x and a value that you must be greater than, give an n for x^2n+1 / (2n+1)! > 1/num"""
	n = 1
	while (x**(2*n+1) / get_factorial(2 * n +1) >  1/num):
		n += 1
	return n

print(get_n(1, 20000))
print(get_2n_1(.1, 2000000))