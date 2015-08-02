#!/usr/bin/python
# This script running countdown script was written by Matthew Moss
# Run 'python countdown.py {datetime} {'script'}
# Run 'python countdown.py for details
#
# Enjoy!

import os
import sys
import time
import datetime

def date_dicts(m):
	dict = {'Mon':0, 'Tue':1, 'Wed':2, 'Thu':3, 'Fri':4, 'Sat':5, 'Sun':6, 'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}
	return dict[m]

def isdate(alarm_time):
	year = int(time.strftime('%Y'))
	m = alarm_time[4:7]
	mon = int(date_dicts(m))
	day = int(alarm_time[8:10])
	Day = alarm_time[0:3]
	if datetime.date(year, mon, day).weekday() != date_dicts(Day):
		print
		print '* Incorrect day for that date - please enter correct date *'
		print 'example: "{0}" (in quotes)' .format(datetime.datetime.now().strftime('%a %b %d %H:%M'))
		print
		sys.exit()
		
def alarm(alarm_time, cmd):
	from datetime import datetime
	while True:
		FMT = '%a %b %d %H:%M:%S'
		c = [' ', '*']
		for item in c:
			dspl_now = time.strftime('%a %b %d %H:%M:%S')
			now = time.strftime('%a %b %d %H:%M')
			remain = datetime.strptime(alarm_time+':00', FMT) - datetime.strptime(dspl_now, FMT)
			output=(item + ' ' + dspl_now + ' '+ item +' timer set to: ' + alarm_time +' '+ item + ' remaining: '+str(remain)+' '+item)
			sys.stdout.write(output)
			sys.stdout.flush()
			backspace = '\b' * len(str(output))
			sys.stdout.write(backspace)
			time.sleep(1)
		if now == alarm_time:
			os.system(cmd)
			sys.exit()

def main():
	if len(sys.argv) == 1:
		print "usage: python timer.py '{0}' 'command' (in quotes)" .format(datetime.datetime.now().strftime('%a %b %d %H:%M'))
		sys.exit(1)
	alarm_time = sys.argv[1]
	isdate(alarm_time)
	cmd = sys.argv[2]
	try:
		time.strptime(alarm_time, '%a %b %d %H:%M')
	except ValueError:
		print
		print 'Alarm time format error!:'
		print 'example: "{0}" (in quotes)' .format(datetime.datetime.now().strftime('%a %b %d %H:%M'))
		print
		sys.exit()
	alarm(alarm_time, cmd)
  
if __name__ == '__main__':
	main()
