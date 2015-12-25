#!/usr/bin/env python
"""
Reducer file
"""

import sys

count = 0
total = 0.0
for line in sys.stdin:
    data = line.strip()
    cost = float(data)
    total += cost
    count += 1
print count, total