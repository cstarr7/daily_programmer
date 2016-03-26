# -*- coding: utf-8 -*-
# @Author: Charles Starr
# @Date:   2016-03-26 17:41:49
# @Last Modified by:   Charles Starr
# @Last Modified time: 2016-03-26 17:43:33

#create a calculator program that will take an input, following normal calculator input (5*5+4)
#and give an answer (29). This calculator should use all four operators.

def calculator():
	try:
		print eval(raw_input('Enter a math problem: '))
	except:
		print 'Please enter a valid mathematical expression.'

calculator()