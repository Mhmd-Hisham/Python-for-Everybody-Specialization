#!/usr/bin/env python3
# Instructor: Dr. Chuck Severance
# Course: Using Python to Access Web Data, University of Michigan, Coursera.

import re
import requests

#In 3 lines.
res = requests.get("http://py4e-data.dr-chuck.net/regex_sum_125524.txt")
open("data.txt", "w+").write(res.text)
print( sum( int(n) for n in re.findall("[0-9]+", open("data.txt").read())) )	



"""
fh = open("data.txt", "w+")
res = requests.get("http://py4e-data.dr-chuck.net/regex_sum_125524.txt")
fh.write(res.text)

numbers = re.findall("[0-9]+", res.text)
numbers = [int(n) for n in numbers]
	
print(sum(numbers))

"""
