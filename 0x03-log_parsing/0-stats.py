#!/usr/bin/python3

"""
Author: Bradley Dillion Gilden
Date: 22-01-2024
"""
import re
from signal import signal, SIGINT


file_size = 0
status_lookup = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}


def print_stats():
    """prints stats read in so far"""
    print("File size: {:d}".format(file_size))
    for code, value in sorted(status_lookup.items()):
        if value != 0:
            print("{}: {:d}".format(code, value))


def signal_handler(signal, frame):
    """handles ctrl + C signal"""
    print_stats()


# set up signal
signal(SIGINT, signal_handler)

if __name__ == '__main__':
    # regex pattern
    pattern = (r'(?:\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' +
               r' - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\] ' +
               r'"GET /projects/260 HTTP/1.1"' +
               r' ([2-5]0[01345]) (\d{1,4})')
    # creating pattern object for reusability
    pobj = re.compile(pattern)
    line_count = 0
    while True:
        instr = input()
        match = pobj.search(instr)
        if (not match):
            continue
        # increment | fill read data
        status_code = match.group(1)
        status_lookup[status_code] += 1
        file_size += int(match.group(2))
        line_count += 1

        if (line_count != 0 and line_count % 10 == 0):
            print_stats()
