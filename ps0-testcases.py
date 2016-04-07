import ps0

#0
print("Odd even examples:")
number = 5
if ps0.odd_even(number):
	print("{} is even.".format(number))
else:
	print("{} is odd.".format(number))

number = 0
if ps0.odd_even(number):
	print("{} is even.".format(number))
else:
	print("{} is odd.".format(number))
	
number = 1
if ps0.odd_even(number):
	print("{} is even.".format(number))
else:
	print("{} is odd.".format(number))

number = 22
if ps0.odd_even(number):
	print("{} is even.".format(number))
else:
	print("{} is odd.".format(number))
	
#1
print("\nDigit counting examples:")

number = 4
print("There is/are {} digit(s) in {}.".format(ps0.digits(number),number))

number = 123
print("There is/are {} digit(s) in {}.".format(ps0.digits(number),number))

number = 36
print("There is/are {} digit(s) in {}.".format(ps0.digits(number),number))

number = 0
print("There is/are {} digit(s) in {}.".format(ps0.digits(number),number))


number = 14223
print("There is/are {} digit(s) in {}.".format(ps0.digits(number),number))


#2
print("\nSum of digits examples:")

number = 4
print("The sum of the digits in {} is {}.".format(number, ps0.sum_digits(number)))

number = 57
print("The sum of the digits in {} is {}.".format(number, ps0.sum_digits(number)))

number = 0
print("The sum of the digits in {} is {}.".format(number, ps0.sum_digits(number)))


number = 902384
print("The sum of the digits in {} is {}.".format(number, ps0.sum_digits(number)))


#3
print("\nSum of integers less than number examples:")

number = 20
print("The sum of the integers less than {} is {}.".format(number, ps0.sum_less_int(number)))

number = 312
print("The sum of the integers less than {} is {}.".format(number, ps0.sum_less_int(number)))

number = 1
print("The sum of the integers less than {} is {}.".format(number, ps0.sum_less_int(number)))


number = 0
print("The sum of the integers less than {} is {}.".format(number, ps0.sum_less_int(number)))


#4
print("\nFactorial examples:")

number = 5
print("{} factorial is {}.".format(number,ps0.factorial(number)))

number = 0
print("{} factorial is {}.".format(number,ps0.factorial(number)))

number = 1
print("{} factorial is {}.".format(number,ps0.factorial(number)))

number = 11
print("{} factorial is {}.".format(number,ps0.factorial(number)))

#5
print("\nChecking factor examples:")

factor =2
if ps0.factor(number, factor):
	print("{} is a factor of {}.".format(factor, number))
else:
	print("{} is not factor of {}.".format(factor, number))

number = 15	
factor = 5
if ps0.factor(number, factor):
	print("{} is a factor of {}.".format(factor, number))
else:
	print("{} is not a factor of {}.".format(factor, number))

#6
print("\nPrime checking examples:")

if ps0.prime(number):
	print("{} is not prime.".format(number))
else:	
	print("{} is prime.".format(number))

number = 1
if ps0.prime(number):
	print("{} is not prime.".format(number))
else:	
	print("{} is prime.".format(number))

number = 35
if ps0.prime(number):
	print("{} is not prime.".format(number))
else:	
	print("{} is prime.".format(number))

number = 11
if ps0.prime(number):
	print("{} is not prime.".format(number))
else:	
	print("{} is prime.".format(number))
	
	
#7
print("\nPerfect numbers examples:")

if ps0.is_perfect(number):
	print("{} is perfect.".format(number))
else:
	print("{} is not perfect.".format(number))

number = 0
if ps0.is_perfect(number):
	print("{} is perfect.".format(number))
else:
	print("{} is not perfect.".format(number))
	
number = 28
if ps0.is_perfect(number):
	print("{} is perfect.".format(number))
else:
	print("{} is not perfect.".format(number))

number = 1
if ps0.is_perfect(number):
	print("{} is perfect.".format(number))
else:
	print("{} is not perfect.".format(number))

#8
print("\nSum of digits as a factor examples:")

if ps0.sum_factor(number):
	print("The sum of the digits in {} is a factor".format(number))
else:
	print("The sum of the digits in {} is not a factor".format(number))

number = 22
if ps0.sum_factor(number):
	print("The sum of the digits in {} is a factor".format(number))
else:
	print("The sum of the digits in {} is not a factor".format(number))

	
number = 12
if ps0.sum_factor(number):
	print("The sum of the digits in {} is a factor".format(number))
else:
	print("The sum of the digits in {} is not a factor".format(number))
