#!/usr/bin/env python
"""
Reducer file
"""

import sys

count_ip = 0
max_count = 0
max_path = None
count_address = 0
dct ={}
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue

    ip, path = data
    if "http://wwww.the-associates.co.uk" in path:
        path = path.replace("http://wwww.the-associates.co.uk", "")
    dct[path] = dct.get(path,0) + 1
    if dct[path] > max_count:
        max_count = dct[path]
        max_path = path
    if ip == "10.99.99.186":
        count_ip += 1
    if path == "/assets/js/the-associates.js":
        count_address += 1


print max_path, "\t", max_count
print "No, of 10.99.99.186 hits:"
print count_ip
print "No, of /assets/js/the-associates.js:"
print count_address