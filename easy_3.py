# -*- coding: utf-8 -*-
# @Author: Charles Starr
# @Date:   2016-03-10 21:18:09
# @Last Modified by:   Charles Starr
# @Last Modified time: 2016-03-10 21:57:07
#write a program that can encrypt texts with an alphabetical caesar cipher. This cipher can ignore numbers, symbols, and whitespace.
#for extra credit, add a "decrypt" function to your program!

class Message(object):
	#class will hold the user input message and have encrypt/decrypt methods
	def __init__(self, message):
		self.raw_message = message

	def encrypt(self, shift):
		#obviously I could use the encode function, but that's too easy
		encrypted_message = ''
		for letter in self.raw_message:
			if str.islower(letter):
				encrypted_message += chr(((ord(letter) - 97) + shift)%26 + 97)
			elif str.isupper(letter):
				encrypted_message += chr(((ord(letter) - 65) + shift)%26 + 65)
			else:
				encrypted_message += letter
		print encrypted_message

	def decrypt(self, shift):
		shift = 26 - shift%26
		decrypted_message = ''
		for letter in self.raw_message:
			if str.islower(letter):
				decrypted_message += chr(((ord(letter) - 97) + shift)%26 + 97)
			elif str.isupper(letter):
				decrypted_message += chr(((ord(letter) - 65) + shift)%26 + 65)
			else:
				decrypted_message += letter
		print decrypted_message

def user_input():
	raw_message = raw_input('Please enter a message for Caesar: ')
	operable_message = Message(raw_message)
	while True:
		cryption = raw_input('(E)ncrypt or (D)ecrypt: ')
		try:
			shift = int(raw_input('Enter the shift: '))
		except:
			print 'Please enter a valid shift'
			continue
		if cryption in ['E', 'e']:
			operable_message.encrypt(shift)
			break
		elif cryption in ['D', 'd']:
			operable_message.decrypt(shift)
			break
		print 'Please enter a valid message operation'

def main():
	user_input()

main()


