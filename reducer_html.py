#!/usr/bin/env python
"""
Reducer file
"""

import sys

count = 0
count_ip = 0
oldKey = None

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue

    ip, path = data
    if oldKey and oldKey != path:
        print oldKey, "\t", count
        oldKey = path
        count = 0

    oldKey = path
    count += 1
    if ip == "10.99.99.186":
        count_ip += 1

if oldKey != None:
    print oldKey, "\t", count
print "No, of 10.99.99.186 hits:"
print count_ip