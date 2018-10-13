#!/usr/bin/env python3
# Instructor: Dr. Chuck Severance
# Course: Using Python to Access Web Data, University of Michigan, Coursera.
#

import urllib.request, urllib.parse, urllib.request
import xml.etree.ElementTree as ET

data = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_42.xml").read() #Sample link
tree = ET.fromstring(data)

print(sum(int(i.text) for i in tree.findall(".//count")))
    
