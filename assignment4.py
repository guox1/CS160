import math
def sqrt(n, error): #define a function, Babylonian algorithm
	guess = n / 2.0; 
	answer = n ** 0.5;
	while abs(answer - guess) > error:
		guess = (guess + (n / guess)) / 2;
	return guess;

user_input = 1;
while(user_input == 1):
	error = 0.0000000000001;
	n = int(input("Enter a positive number:  "));
	print("The guess answer is " + str(sqrt(n, error)));
	print("The right answer is " + str(math.sqrt(n)));
	user_input = (int(input("To continue? (1 - yes, 0 - no): "))); 
