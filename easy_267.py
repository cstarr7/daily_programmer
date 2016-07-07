# -*- coding: utf-8 -*-
# @Author: Charles Starr
# @Date:   2016-07-06 23:20:28
# @Last Modified by:   Charles Starr
# @Last Modified time: 2016-07-06 23:53:49

#https://www.reddit.com/r/dailyprogrammer/comments/4jom3a/20160516_challenge_267_easy_all_the_places_your/

def input_place():
	#ask user what place their dog got, check validity, return int
	while True:
		fail_msg = 'Enter a positive integer'
		try:
			user_input = int(raw_input('What place did your dog get?'))
		except:
			print fail_msg
		return user_input

def not_places(place, show_size=100):
	#returns list of places that your dog didn't finish
	place_list = []
	for not_place in range(1, show_size+1):
		if place == not_place:
			continue
		place_string = str(not_place)
		suffix = 'th'
		important_digits = place_string
		if len(place_string) > 1:
			important_digits = place_string[-2:]
		if important_digits[-1] == '1' and  important_digits != '11':
			suffix = 'st'
		elif important_digits[-1] == '2' and important_digits != '12':
			suffix = 'nd'
		elif important_digits[-1] == '3' and important_digits != '13':
			suffix = 'rd'
		place_list.append(place_string + suffix)
	return place_list

def main():
	size = input_place()
	print not_places(size)

main()



