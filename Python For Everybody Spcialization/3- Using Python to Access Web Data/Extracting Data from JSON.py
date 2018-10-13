#!/usr/bin/env python3
# Instructor: Dr. Chuck Severance
# Course: Using Python to Access Web Data, University of Michigan, Coursera.
#

import json
import urllib.request, urllib.parse, urllib.request

url = input("Enter location: ")

print("Retrieving", url)
data = urllib.request.urlopen(url).read().decode()

print("Retrieved {} characters".format(len(data)))
info = json.loads(data)


s = 0
count = 0
for dictionary in info["comments"]:
    count += 1
    s += int(dictionary["count"])

print("Count:", count)
print("Sum:", s)
