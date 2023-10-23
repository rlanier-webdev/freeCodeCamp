'''
FreeCodeCamp's Scientific Computing with Python - Time Calculator

Write a function named add_time that takes in two required parameters and one optional parameter.

Author: RaShunda Williams
Completed: 06-17-23
'''

# imports
from datetime import datetime, timedelta

# a start time in the 12-hour clock format (ending in AM or PM)
start = '11:00 PM'

# a duration time that indicates the number of hours and minutes
duration = '03:05'

# (optional) a starting day of the week, case insensitive
day_of_week = {
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday'
}

def add_time(start, duration, day_of_week=None):
    # Parse the time string into a datetime object
    start = datetime.strptime(start,'%I:%M %p')

    # convert duration from string to time
    h, m = duration.split(':')
    duration = timedelta(hours=int(h),minutes=int(m))
    
    # add the duration time to the start time 
    result = start + duration

    # If the result will be the next day, it should show (next day) after the time.
    # convert result to 12 oclock format
    # if pm to am then next day


    # If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.
    # If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result.
    # The day of the week in the output should appear after the time and before the number of days later.

    return result.strftime("%I:%M %p")

add_time('12:59 AM','125:00')
