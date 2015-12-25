"""
Mapper for a Udacity Hadoop course
"""

import sys

for line in sys.stdin:
        # strip off extra whitespace, split on tab and put the data in an array
        data = line.strip().split("\t")
        if len(data) == 6:
            date, time, store, item, cost, payment = data
        # Now print out the data that will be passed to the reducer
            print "{0}\t{1}".format(store, cost)