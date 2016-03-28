def odd_even(number):
	if number%2 == 0:
		return True
	



def digits(number):
	number = str(number)
	count = 0
	for x in number:
		count += 1
	return count
	
	
def sum_digits(number):
	total = 0
	
	for x in str(number):
		total += int(x)

	return total
	


def sum_less_int(number):
	count = 1
	list = []
	while count < number:
		list.append(str(count))
		count += 1
	list = ' + '.join(list)
	
	totalLess = 0
	while number > 0:
		totalLess += number - 1
		number -= 1
	
	return('{}, which is {}'.format(totalLess,list))
	

def factorial(number):
	originalNumber = number
	totalFactorial = 1
	while number > 1:
		totalFactorial *= number - 1
		number -= 1
	return('{}, which is {}!'.format(totalFactorial,originalNumber))
	

def factor(number):
	factor = -1
	while factor < 0:
		factor = int(raw_input("Enter a factor to check (must be positive): "))
		
	if number%factor == 0:
		return True

			
			
			

def prime(number):
	count = 2
	while count < number:
 		if number%count == 0:
 			return True
	 		exit()
 		count+=1

	
	
	
	
def is_perfect(number):
	totalFactors = 0
	count = 1
	while count < number:
 			if number%count == 0:
 				totalFactors += count
 			count += 1
 			
	if totalFactors == number:
		return True

	
def sum_factor(number):	
	total = sum(number)
	if number%total == 0:
		return True

		
		
		
		
		
