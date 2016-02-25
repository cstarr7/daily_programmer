#create a program that will ask the users name, age, and reddit username. 
#have it tell them the information back, in the format
#your name is (blank), you are (blank) years old, and your username is (blank)

def get_user_info():
	#ask for each parameter and store in a variable
	name = raw_input('What is your name?')
	age = raw_input('How old are you?')
	user_name = raw_input('What is your reddit username?')
	#put message together and print it
	msg = ('your name is ' + name + ', your are ' + age + 
		' years old, and you username is ' + user_name)
	print msg

get_user_info()