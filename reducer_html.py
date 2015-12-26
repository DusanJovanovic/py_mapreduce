#!/usr/bin/env python
"""
Reducer file
"""

import sys

count = 0
count_ip = 0
oldKey = None
max_count = 0
max_path = None
count_address = 0
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue

    ip, path = data
    if oldKey and oldKey != path:
        if count > max_count:
            max_count = count
            max_path = oldKey
        oldKey = path
        count = 0

    oldKey = path
    count += 1
    if ip == "10.99.99.186":
        count_ip += 1
    if path == "/assets/js/the-associates.js":
        count_address += 1


print max_path, "\t", max_count
print "No, of 10.99.99.186 hits:"
print count_ip
print "No, of /assets/js/the-associates.js:"
print count_ip