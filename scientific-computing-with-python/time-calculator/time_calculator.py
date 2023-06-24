'''
FreeCodeCamp's Scientific Computing with Python - Time Calculator

Write a function named add_time that takes in two required parameters and one optional parameter.

Author: RaShunda Williams
Completed:
'''

# imports
from datetime import datetime, time, timedelta

# (optional) a starting day of the week, case insensitive
day = ''

def add_time(start, duration):
    # Parse the time string into a datetime object
    start = datetime.strptime(start,'%I:%M %p')

    # convert duration from string to time
    h, m = duration.split(':')
    duration = timedelta(hours=int(h),minutes=int(m))
    
    # add the duration time to the start time 
    result = start + duration
    n = result.day

    # If the result will be the next day, it should show (next day) after the time.
    if n == 2:
        print(result.strftime('%I:%M %p'), '(next day)')
    else:
        print(result.strftime('%I:%M %p'))

    # If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.
    if n > 2:
        print(result.strftime('%I:%M %p'), f'({n-1} days later)')

    # If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result.
    # The day of the week in the output should appear after the time and before the number of days later.

    #return result.strftime("%I:%M %p")
    return result

add_time('11:59 PM','72:00')