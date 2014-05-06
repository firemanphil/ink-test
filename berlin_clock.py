#!/usr/bin/env python
import sys
from time import localtime,strptime,strftime
import datetime
import time

def get_hour_string(hours):
    num_red_lights,remainder = divmod(hours,5)
    first_row = ('R'*num_red_lights).ljust(4,'O')
    second_row = ('R'*remainder).ljust(4,'O')
    return first_row + ' ' + second_row

def get_min_string(mins):
    num_lights_first_row, num_lights_second_row = divmod(mins,5)
    first_row = ''
    for i in range(num_lights_first_row):
        if (i+1)%3 == 0:
            first_row += 'R'
        else:
            first_row += 'Y'
    first_row = first_row.ljust(11,'O')
    second_row = ('Y'* num_lights_second_row).ljust(4,'O')
    return first_row + ' ' + second_row

def convert_to_berlin_clock_string(time_string):
    try:
        time_to_convert = strptime(time_string,'%H:%M:%S')
        (hour,min,sec) = (time_to_convert[3], time_to_convert[4], time_to_convert[5])
    except ValueError:
        if time_string.find('24')==0:
            time_to_convert = strptime('00:'+':'.join(time_string.split(':')[1:]),'%H:%M:%S')
            (hour,min,sec) = (24, time_to_convert[4], time_to_convert[5])
        else:
            print "Couldn't parse the date you gave me. Make sure it's in this format 'HH:MM:SS'"
            exit(1)
    except:
        print "Couldn't parse the date you gave me. Make sure it's in this format 'HH:MM:SS'"
        exit(1)

        
    return ' '.join((time_string,'Y' if sec%2==0 else 'O',get_hour_string(hour),get_min_string(min)))

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print 'You entered too many arguments - usage is \'./berlinUhrClock.py TIME\' where TIME is in the following format: \'HH:MM:SS\''
        exit(1)

    if len(sys.argv) == 1:
        while True:
            print convert_to_berlin_clock_string(strftime("%H:%M:%S",localtime()))
            time.sleep(1)
    else:
        print convert_to_berlin_clock_string(sys.argv[1].strip())


