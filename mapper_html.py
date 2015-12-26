#!/usr/bin/env python
"""
Mapper for a Udacity Hadoop course
"""

import sys

for line in sys.stdin:
    # strip off extra whitespace, split on tab and put the data in an array
    data = line.strip().split(" ")
    if len(data) == 10:
        ip, client_id, client_uname, date_time, time_zone, get, path, req, status, size = data
    # Now print out the data that will be passed to the reducer
        if "http://wwww.the-associates.co.uk" in path:
            path = path.replace("http://wwww.the-associates.co.uk", "")
        print "{0}\t{1}".format(ip, path)

##with open("pypy.txt", "r") as infile:
##    for line in infile:
##        data = line.strip().split(" ")
##        print data