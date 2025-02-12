# How to display Python Dates
# import module -> import datetime

import datetime

x = datetime.datetime.now() 
y = datetime.date.today() # year, month, and day.
# The date contains year, month, day, hour, minute, second, and microsecond.
print(x)
print(y)
print(x.year) #display year
print(x.day) #display days
print(x.minute) #display minute 

# Creating Date Objects
# To create a date, we can use the datetime()

x = datetime.datetime(2020, 5, 17)
# The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone)
print(x)


# The strftime() Method
# The datetime object has a method for formatting date objects into readable strings.
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B")) #June
print(x.strftime("%A")) #Friday


# Lab tasks:
from datetime import date, timedelta

#1
dt = date.today() - timedelta(5)
print(f"Current date: {date.today()}. \n5 days before current date: {dt}")

#2
today = date.today()
yesterday = today - timedelta(1)
tomorrow = today + timedelta(days = 1)
print(today, yesterday, tomorrow)
print(today.day, yesterday.day, tomorrow.day)

#3 
dt = datetime.datetime.today().replace(microsecond=0)
# Print the current date and time (with microseconds removed)
print(dt)

#4
date1 = datetime.datetime.now()
date2 = datetime.datetime.strptime('2025-02-12 11:00:00', '%Y-%m-%d %H:%M:%S')

#strptime means string parser, this will convert a string format to datetime.
# datetime.strptime('2019-08-09 01:01:01', "%Y-%m-%d %H:%M:%S")
# datetime.datetime(2019, 8, 9, 1, 1, 1)//Result

#strftime means string formatter, this will format a datetime object to string format.
# sample_date=datetime.strptime('2019-08-09 01:01:01', "%Y-%m-%d %H:%M:%S")
# datetime.strftime(sample_date, "%Y-%d-%m %H:%M:%S")
# '2019-09-08 01:01:01'//Result

time_d = date1- date2
time_d = time_d.days * 24 * 3600 + time_d.seconds
print(time_d)

