# -*- coding: utf-8 -*-
# @Author: Charles Starr
# @Date:   2016-03-10 22:27:05
# @Last Modified by:   Charles Starr
# @Last Modified time: 2016-03-10 23:06:38
'''
Welcome to cipher day!
For this challenge, you need to write a program that will take the scrambled words from this post, and compare them against THIS WORD LIST to unscramble them. For bonus points, sort the words by length when you are finished. Post your programs and/or subroutines!
Here are your words to de-scramble:
mkeart
sleewa
edcudls
iragoge
usrlsle
nalraoci
nsdeuto
amrhat
inknsy
iferkna
'''
#I'm going to brute force this using dictionaries, probably won't be pretty

class Words(object):
	#this will contain the wordlist in dictionary format
	def __init__(self, dict_file):
		self.dic_list = self.load_words(dict_file)

	def load_words(self, dict_file):
		dictionary_list = {}
		with open(dict_file) as word_list:
			for word in word_list:
				word = word[:-1]
				dictionary_list[word] = {}
				for letter in word:
					if not letter in dictionary_list[word].iterkeys():
						dictionary_list[word][letter] = 1
					else:
						dictionary_list[word][letter] += 1
		return dictionary_list

def build_dictionaries(word_file, scramble_file):
	#helper to construct both sets of dictionaries
	words = Words(word_file)
	scrambles = Words(scramble_file)
	return words, scrambles

def match_em(word_dic, scramble_dic):
	#finds the dictionaries that match
	unscrambled = []
	for scramble_key in scramble_dic.dic_list.iterkeys():
		for word_key in word_dic.dic_list.iterkeys():
			if scramble_dic.dic_list[scramble_key] == word_dic.dic_list[word_key]:
				unscrambled.append((scramble_key, word_key))
	return unscrambled

def main(word_file, scramble_file):
	word_dic, scramble_dic = build_dictionaries(word_file, scramble_file)
	unscrambled = match_em(word_dic, scramble_dic)
	print unscrambled

main('d3_wordlist.txt','d3_scramble.txt')

