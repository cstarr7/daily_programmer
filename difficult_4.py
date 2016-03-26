# -*- coding: utf-8 -*-
# @Author: Charles Starr
# @Date:   2016-03-26 17:48:03
# @Last Modified by:   Charles Starr
# @Last Modified time: 2016-03-26 18:16:35

#today, your challenge is to create a program that will take a series 
#of numbers (5, 3, 15), and find how those numbers can add, subtract, 
#multiply, or divide in various ways to relate to eachother. 
#This string of numbers should result in 5 * 3 = 15, or 15 /3 = 5, 
#or 15/5 = 3.

import itertools

def main():
	raw_list = user_input()
	integer_list = prepare_list(raw_list)
	calculation_comparison(integer_list)

def user_input():
	#collects list from user
	return raw_input('Enter a comma separated list of integers: ')

def prepare_list(raw_list):
	#formats the raw comma separated string
	try:
		return [int(i) for i in raw_list.split(',')]
	except:
		print 'Enter a valid list of integers.'
		return []

def calculation_comparison(integer_list):
	#use itertools to loop through combinations from list
	relation_list = []
	for pair in itertools.combinations(integer_list, 2):
		pair_sum = pair[0] + pair[1]
		if pair_sum in relation_list:
			relation_list.append(message_generator(pair[0],pair[1],
													pair_sum, '+'))
		pair_difference_one = pair[0] - pair[1]
		if pair_difference_one in integer_list:
			relation_list.append(message_generator(pair[0],pair[1],
													pair_difference_one, '-'))
		pair_difference_two = pair[1] - pair[0]
		if pair_difference_two in integer_list:
			relation_list.append(message_generator(pair[1],pair[0],
													pair_difference_two, '-'))
		pair_product = pair[0]*pair[1]
		if pair_product in integer_list:
			relation_list.append(message_generator(pair[0], pair[1],
													pair_product, '*'))
		pair_quotient_one = pair[0]/pair[1]
		if pair_quotient_one in integer_list:
			relation_list.append(message_generator(pair[0], pair[1],
													pair_quotient_one, '/'))
		pair_quotient_two = pair[1]/pair[0]
		if pair_quotient_two in integer_list:
			relation_list.append(message_generator(pair[1], pair[0],
													pair_quotient_two, '/'))
	for relation in relation_list:
		print relation

def message_generator(int_a, int_b, answer, operator):
	#formats relationships and returns them for addition to list
	return str(int_a) + ' %s ' % operator + str(int_b) + ' = ' + str(answer)

main()
