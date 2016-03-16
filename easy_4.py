# -*- coding: utf-8 -*-
# @Author: Charles Starr
# @Date:   2016-03-16 00:26:32
# @Last Modified by:   Charles Starr
# @Last Modified time: 2016-03-16 00:44:14

#You're challenge for today is to create a random password generator!
#For extra credit, allow the user to specify the amount of passwords 
#to generate.
#For even more extra credit, allow the user to specify the length of 
#the strings he wants to generate!

import string
import random

def main():
	number, length = user_input()
	password_list = password_gen(length, number)
	file_generator(password_list)

def user_input():
	#collects user input, validates integer status
	while True:
		number = raw_input('Please enter the number of passwords to generate: ')
		length = raw_input('Please enter the desired password length: ')
		try:
			return int(number), int(length)
		except:
			print 'Enter a valid integer for both parameters.'

def password_gen(number, length):
	#generates the requested number of passwords
	password_list = []
	for i in range(number):
		password_list.append(''.join(
		[random.choice(string.printable) for x in range(length)]))
	return password_list

def file_generator(password_list):
	#creates text file filled with passwords.
	with open('passwords.txt', 'wb') as pass_file:
		for password in password_list:
			pass_file.write(password+'\r\n')

main()


