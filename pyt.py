#!/usr/bin/python

import time
import os
import webbrowser

print "MENU CONTROLLED PROGRAM"

x='''
press 1:To check current date and time:
press 2:reboot os:
press 3:to create a user in your current os:
press 4:to open or to search something in google:
press 5:to search your data on google and print url of first page:
press 6:to check ram and cpu info:
press 7:to login your facebook account and update the status Hello:
press 8:to scan all ip addresses in your network:
'''
print "                            "
print "-------------*--------------"
print x
 
choice=int(raw_input())

if choice==1:
	print "Current date and time"
	print time.ctime()
elif choice==2: 
	print "Reboot os" 
	os.system('reboot')
elif choice==3:
	print "Create new user account"
	x=raw_input('username ')
	os.system('useradd '+x)
	os.system('passwd '+x)
elif choice==4:
	print "To open and search on google"
	x=raw_input('enter data to search ')
	webbrowser.open_new_tab('https://www.google.com/search?q='+x)
elif choice==5:
	print "To open and search on google"
        x=raw_input('enter data to search ')
        y=webbrowser.open_new_tab('https://www.google.com/search?q='+x)
	print (y)
elif choice==6:
	print "Information of CPU"
	os.system('cat /proc/cpuinfo')
	print "                    "
	print "Information of RAM"
	os.system('cat /proc/meminfo')
elif choice==7:
	print "Login to facebook"
        webbrowser.open_new_tab('https://www.facebook.com/login')
	x=raw_input()
	print x	
elif choice==8:
	print "Available ip addresses in network"
		
else: 
	print "no choice"

