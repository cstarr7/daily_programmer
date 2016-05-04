# -*- coding: utf-8 -*-
# @Author: Charles Starr
# @Date:   2016-05-04 16:19:42
# @Last Modified by:   Charles Starr
# @Last Modified time: 2016-05-04 18:48:53

#https://www.reddit.com/r/dailyprogrammer/comments/4hhiu8/20160502_challenge_265_easy_permutations_and/
#could use itertools but I'll try to put it together without
import copy

class Perm_comb(object):
	#this object will hold the number list and return permutations and/or combinations
	def __init__(self, number_list):
		self.numbers = number_list

	def permutations(self):
		#creates a list of all permutations in self.numbers
		perm_list = [[]]
		for i in self.numbers:
			first_temp = []
			for partial_perm in perm_list:
				second_temp = [copy.copy(partial_perm) for x in range(len(partial_perm), len(self.numbers),1)]
				for j in self.numbers:
					if j not in partial_perm:
						to_add = second_temp.pop()
						to_add.append(j)
						first_temp.append(to_add)
			perm_list = first_temp
		return perm_list

	def indexed_permutations(self, key):
		#key is index value
		return self.permutations()[key]

	def combinations(self, count):
		#generates all combinations of length count for number list
		perm_list = [[]]
		for i in self.numbers:
			temp_list = [copy.copy(x) for x in perm_list if len(x) < count]
			for combo in temp_list:
				combo.append(i)
			perm_list.extend(temp_list)
		perm_list = [x for x in perm_list if len(x) == count]
		return sorted(perm_list)

	def indexed_combinations(self,count,key):
		#key is index value
		return self.combinations(count)[key]


		#creates a list of all combinations in self.numbers

def main():
	number_list = Perm_comb(range(0,9,1))
	print number_list.indexed_combinations(4,111)


