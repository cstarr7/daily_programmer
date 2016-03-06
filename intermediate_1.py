#Create a menu driven program
#Using the menu drive program allow a user to add/delete items
#The menu should be based on an events calender where users enter the events by hour
#No events should be hard-coded.
import datetime

class Event(object):
	#Event object contains details about event 
	def __init__(self, name, date, time, description):
		self.name = name
		self.date = date
		self.time = time
		self.description = description

	def __str__(self):
		return ("Name: %s \nDate: %s \nTime: %s \nDescription: %s \n" 
		% (self.name, self.date.isoformat(), self.time.isoformat(), self.description))

	def __lt__(self,other):
		self_datetime = datetime.datetime.combine(self.date, self.time)
		other_datetime = datetime.datetime.combine(other.date, other.time)
		return self_datetime < other_datetime

class Event_Calendar(object):
	#container for events with methods to add, edit and delete events
	def __init__(self):
		self.calendar = []

	def add_event(self):
		name = raw_input('Please enter event name: ')
		date = raw_input('Please enter event date (YYYY/MM/DD): ')
		time = raw_input('Please enter event time (Hour only (24)): ')
		description = raw_input('Briefly describe the event: ')
		date = format_date(date)
		time = format_time(time)
		new_event = Event(name, date, time, description)
		print 'New event details: '
		print str(new_event)
		self.calendar.append(new_event)
		self.calendar.sort()

	def edit_event(self, event_index):
		selected_event = self.calendar[event_index]
		print selected_event
		print 'Which attributes would you like to edit?'
		print '1. Name'
		print '2. Date'
		print '3. Time'
		print '4. Description'
		desired_edits = raw_input('Please enter choices separated by commas: ')
		edit_list = desired_edits.split(',')
		if '1' in edit_list:
			print 'The current event name is ' + selected_event.name
			new_name = raw_input('Please enter new event name: ')
			selected_event.name = new_name
		if '2' in edit_list:
			print 'The current event date is ' + selected_event.date.isoformat()
			new_date = raw_input('Please enter new event date (YYYY/MM/DD): ')
			selected_event.date = format_date(new_date)
		if '3' in edit_list:
			print 'The current event time is ' + selected_event.time.isoformat()
			new_time = raw_input('Please enter new event time (hour only (24)): ')
			selected_event.time = format_time(new_time)
		if '4' in edit_list:
			print 'The current event description is "' + selected_event.description +'"'
			new_description = raw_input('Please enter new event description: ')
			selected_event.description = new_description
		print 'Modified event details: '
		print str(selected_event)
		self.calendar.sort()

	def delete_event(self, event_index):
		throwaway = self.calendar.pop(event_index)
		print 'Selected event has been removed from the calendar.'

	def display_events(self):
		for event, number in zip(self.calendar,range(1,len(self.calendar)+1)):
			print 'Event #%s' % number
			print event

def menu(calendar):
	#implements a text menu with options for event calendar
	print 'What action would you like to take?'
	print '1. Add new event'
	print '2. Edit existing event'
	print '3. Delete existing event'
	print '4. View Existing events'
	print '5. Quit'
	selection = raw_input('Please enter a number: ')
	if selection == '1':
		calendar.add_event()
		return calendar
	elif selection == '2':
		calendar.display_events()
		to_edit = raw_input('Select an event to edit: ')
		edit_index = int(to_edit) - 1 #convert input to index value
		if (0 <= edit_index <= len(calendar.calendar)):
			calendar.edit_event(edit_index)
		return calendar
	elif selection == '3':
		calendar.display_events()
		to_delete = raw_input('Select an event to edit: ')
		delete_index = int(to_delete) - 1 #convert input to index value
		if (0 <= delete_index <= len(calendar.calendar)):
			calendar.delete_event(delete_index)
		return calendar
	elif selection == '4':
		calendar.display_events()
		return calendar
	elif selection == '5':
		return
	else:
		print 'Invalid input, please try again.'
		return calendar

def format_time(time):
	#helper to make sure time is added correctly
	while True:
		try:
			return datetime.time(hour=int(time))
		except:
			time = raw_input('Invalid time format used, please re-enter time (24h): ')

def format_date(date):
	#helper to extract date and time from strings and return datetime object
	while True:
		try:
			date_parse = date.split('/')
			return datetime.date(int(date_parse[0]), int(date_parse[1]), 
				int(date_parse[2]))
		except:
			date = raw_input('Invalid date format used, please re-enter date (YYYY/MM/DD): ')

def main():
	#calls menu to start program. That's it.
	calendar = Event_Calendar()
	while calendar:
		calendar = menu(calendar)
main()