#!/usr/bin/env python
from  berlin_clock import convert_to_berlin_clock_string
from sys import stdout, argv
from time import localtime,strftime
from termcolor import colored
import time

def print_colored_berlin_clock_string(time_string):
    string_rep = convert_to_berlin_clock_string(time_string)
    stdout.write(string_rep+' ')
    stdout.write('>')
    for char in ' '.join(string_rep.split(' ')[1:]):
        if char == ' ':
            stdout.write('< >')
        elif char == 'Y':
            stdout.write(colored(' ',on_color='on_yellow'))
        elif char == 'R':
            stdout.write(colored(' ',on_color='on_red'))
        elif char == 'O':
            stdout.write(' ')
    stdout.write('<')
    stdout.write('\r')
    stdout.flush()


if len(argv) == 2:
    print_colored_berlin_clock_string(argv[1])
elif len(argv) == 1:
    while True:
        print_colored_berlin_clock_string(strftime("%H:%M:%S",localtime()))
        time.sleep(1)
