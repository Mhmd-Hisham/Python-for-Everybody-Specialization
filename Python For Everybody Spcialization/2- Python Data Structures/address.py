#!/usr/bin/env python3
# Instructor: Dr. Chuck Severance
# Course: Python Data Strucutres, University of Michigan, Coursera.

import sys
import requests

res = requests.get("https://www.py4e.com/code3/mbox-short.txt")
print("Status:", res.status_code)
data = res.text

fh = data.splitlines()
count = 0
for line in fh:
    if line.startswith("From:"):
        continue
    if line.startswith("From"):
        count += 1
        print(line.split()[1])

print("There were", count, "lines in the file with From as the first word")
    
