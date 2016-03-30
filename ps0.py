def odd_even(number):
	"""This function determines if the argument is odd or even and returns true if even"""
	if number%2 == 0:
		return True
	else:
		return False
		

def digits(number):
	"""This function returns the number of digits in the argument"""
	number = str(number)
	count = 0
	for x in number:
		count += 1
	return count
	
	
def sum_digits(number):
	"""This function returns the sum of every digit in the argument"""
	total = 0
	
	for x in str(number):
		total += int(x)

	return total


def sum_less_int(number):
	"""This function returns the sum of all the integers less than the argument"""
	totalLess = 0
	while number > 0:
		totalLess += number - 1
		number -= 1
	
	return totalLess
	

def factorial(number):
	"""This function returns the factorial of the argument"""
	totalFactorial = 1
	while number > 1:
		totalFactorial *= number - 1
		number -= 1
	return totalFactorial
	

def factor(number, factor):
	"""This function takes in two arguments and checks if the 2nd argument is a factor of the first. If it is a factor the function returns true."""
	if number%factor == 0:
		return True
	else:
		return False
			

def prime(number):
	"""This function checks if the argument is prime and returns true if it is not prime"""
	count = 2
	while count < number:
 		if number%count == 0:
 			return True
	 		exit()
 		count+=1
 	else:
 		return False

	
	
def is_perfect(number):
	"""This function checks if the argument is a perfect number"""
	totalFactors = 0 #keeps track of the factors
	count = 1
	while count < number:
 			if number%count == 0:
 				totalFactors += count #if the number the count is at is a factor (there is no remainder), then the count gets added so that the total factors is kept track of
 			count += 1
 			
	if totalFactors == number:
		return True
	else:
		return False
	
	
def sum_factor(number):	
	"""This function calls upon the sum function, and adds the digits of the argument. It then checks if the sum is a factor of the argument, and returns false if it is a factor."""
	total = sum(number)
	if number%total == 0:
		return True
	else:
		return False
		
		
		
		
		
