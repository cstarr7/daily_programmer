# -*- coding: utf-8 -*-
# @Author: Charles Starr
# @Date:   2016-05-13 16:21:31
# @Last Modified by:   Charles Starr
# @Last Modified time: 2016-05-14 14:32:46

#https://www.reddit.com/r/dailyprogrammer/comments/4htg9t/20160504_challenge_265_easy_permutations_and/
#what is the 12345678901234 permutation index of 42-length list
#what is the permutation number of:  25 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 35 32 36 34 39 29 27 33 26 37 40 30 31 41 28 38

import math

def permutation(length, index):
	original_list = range(0,length)
	permutated_list = []
	while original_list:
		tier = int(math.ceil(float(index)/math.factorial(len(original_list)- 1)))
		permutated_list.append(original_list.pop(tier - 1))
		index -= math.factorial(len(original_list))*(tier - 1)
	print permutated_list

def permutation_index(permutation):
	index = 0
	while permutation:
		tier_size = math.factorial(len(permutation) - 1)
		index += sorted(permutation).index(permutation[0]) * tier_size
		permutation.pop(0)
	print index
#permutation_index([25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,35,32,36,34,39,29,27,33,26,37,40,30,31,41,28,38])

def combination_number(size, combination):
	choice_list = range(0,size)
	index = 0
	for k, i in enumerate(combination, 0):
		for j in range(0,len(choice_list)):
			if i != choice_list[j]:
				index += combinations(len(choice_list[j:])-1, len(combination[k:])-1)
			else:
				choice_list = choice_list[j+1:]
				break
	print index

def combinations(n, k):
	return math.factorial(n)/math.factorial(n-k)/math.factorial(k)

combination_number(100,[15,25,35,45,55,65,85])