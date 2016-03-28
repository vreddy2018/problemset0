import ps0


function = raw_input("What function do you want to run? \n0. Odd or even \n1. Number of digits \n2. Sum of digits \n3. Sum of integers less \n4. Factorial \n5. Check factor \n6. Prime check \n7. Check if a number is perfect \n8. Sum of digits as a factor \nGive only the number: ")


number = -1
while number < 0:
	number = int(raw_input("Enter the number you want to use (Must be a non-negative integer): "))



if function == "0":
	if ps0.odd_even(number):
		print("Even")
	else:
		print("Odd")
	
	
elif function == "1":
	print(ps0.digits(number))
	
	
elif function == "2":
	print(ps0.sum_digits(number))
	
	
elif function == "3":
	print(ps0.sum_less_int(number))
	
	
elif function == "4":
	print(ps0.factorial(number))
	
	
elif function == "5": 
	if ps0.factor(number):
		print("It is a factor")
	else:
		print("It is not a factor")
	
	
elif function == "6":
	if ps0.prime(number):
		print("The number is not prime")
	else:	
		print("The number is prime")
	
	
elif function == "7":
	if ps0.is_perfect(number):
		print("The number is perfect")
	else:
		print("The number is not perfect")
		
		
elif function == "8":	
	if ps0.sum_factor(number):
		print("Sum is factor")
	else:
		print("Sum is not a factor")
	
	
else:
	print("Not one of the functions")
	exit()

