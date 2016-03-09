# -*- coding: utf-8 -*-
# @Author: Charles Starr
# @Date:   2016-03-07 17:27:18
# @Last Modified by:   Charles Starr
# @Last Modified time: 2016-03-08 23:44:00
#easy_2
#Hello, coders! An important part of programming is being able to apply 
#your programs, so your challenge for today is to create a calculator 
#application that has use in your life. It might be an interest 
#calculator, or it might be something that you can use in the classroom.
#For example, if you were in physics class, you might want to make a 
#F = M * A calc.

#I'm just going to make a BMI calculator for Americans

def calculate_bmi(height, weight):
	#converts to metric and calculates BMI
	height_meters = height * 0.0254 #convert inches to meters
	weight_kilos = weight *0.453592 #convert lbs. to kilos
	bmi = weight_kilos/height_meters**2
	return bmi

def user_input():
	#gets user input and ships it to calculator to get bmi
	while True:
		height = raw_input('Please enter height in inches: ')
		weight = raw_input('Please enter weight in pounds: ')
		try: #make sure only numeric datatypes used and no 0 heights
			return float(height), float(weight)
		except:
			print 'Please enter a valid height and weight.'

def give_advice(bmi):
	#gives user blunt health advice based on BMI
	if bmi < 18.5:
		print 'You need to gain weight!'
	elif bmi >= 25:
		print 'You need to lose weight!'
	else:
		print 'You are a healthy weight.'

def main():
	height, weight = user_input()
	bmi = calculate_bmi(height, weight)
	print 'The calculated BMI is %.2f' % bmi
	give_advice(bmi)

main()