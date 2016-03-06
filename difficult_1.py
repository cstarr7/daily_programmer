#we all know the classic "guessing game" with higher or lower prompts. 
#lets do a role reversal; you create a program that will guess numbers between 1-100,
#and respond appropriately based on whether users say that the number is too high 
#or too low. Try to make a program that can guess your number based on user input 
#and great code!

import random

def number_guesser(low=0, high=100):#only function, has default 0-100 but can change
	
	while True:
		if low == high:#Only one number left, which must be correct
			print 'Your number is ' + str(low)
			break
		if high < low:#User input led to low being larger than high
			print 'You cheated!'
			break
		current_guess = random.randint(low, high)
		print 'Is your number ' + str(current_guess)
		user_input = raw_input('Is guess high, low, or correct?: ')
		if user_input == 'high':
			high = current_guess - 1
		elif user_input == 'low':
			low = current_guess + 1
		elif user_input == 'correct':
			print 'Your number was ' + str(current_guess)
			print 'Man, I\'m good'
			break
		else:
			print 'Invalid input, please try again'

number_guesser()
