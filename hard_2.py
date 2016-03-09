# -*- coding: utf-8 -*-
# @Author: Charles Starr
# @Date:   2016-03-08 23:51:13
# @Last Modified by:   Charles Starr
# @Last Modified time: 2016-03-09 00:14:55

#Your mission is to create a stopwatch program. 
#this program should have start, stop, and lap options, 
#and it should write out to a file to be viewed later.
import datetime as dt

class Stopwatch(object):
	#object contains time and does simple operations
	def __init__(self):
		self.start_time = None

	def start(self):
		if self.start_time == None:
			self.start_time = dt.datetime.utcnow()
		else:
			print 'The watch is already running.'

	def lap(self):
		if not self.start_time == None:
			delta = dt.datetime.utcnow() - self.start_time
			print delta.total_seconds()
			print 'The clock is still running'
		else:
			print 'The clock is not running'

	def stop(self):
		if not self.start_time == None:
			delta = dt.datetime.utcnow() - self.start_time()
			self.start_time = None
			print delta.total_seconds()
			print 'The clock is stopped'
		else:
			print 'The clock is not running.'

	def reset(self):
		if not self.start_time == None:
			self.start_time = dt.datetime.utcnow()
			print 'The clock has restarted.'
		else:
			print 'The clock is not running.'

def menu(stopwatch):
	#displays a menu for stopwatch operations
	while True:
		print 'Stopwatch options:'
		print '1. Start'
		print '2. Lap'
		print '3. Stop'
		print '4. Reset'
		print '5. Quit'
		user_choice = raw_input('Select an operation: ')
		if user_choice == '1':
			stopwatch.start()
		elif user_choice == '2':
			stopwatch.lap()
		elif user_choice == '3':
			stopwatch.stop()
		elif user_choice == '4':
			stopwatch.reset()
		elif user_choice == '5':
			break
		else:
			print 'Please enter a valid menu option.'

def main():
	#creates stopwatch and sends it to the menu
	stopwatch = Stopwatch()
	menu(stopwatch)

main()