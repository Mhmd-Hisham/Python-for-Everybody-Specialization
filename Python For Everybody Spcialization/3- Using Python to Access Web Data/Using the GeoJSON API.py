#!/usr/bin/env python3
# Author: Mohamed Hisham El-Banna
# Submission datetime: 'Mon Sep 10 03:23:48 EET 2018'
#
# Instructor: Dr. Chuck Severance
# Course: Using Python to Access Web Data, University of Michigan, Coursera.

import json
import urllib.request, urllib.parse, urllib.error

# Note that Google is increasingly requiring keys
# for this API
# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
serviceurl = "http://py4e-data.dr-chuck.net/geojson?"

# address = "Georgetown University Law Center"
address = input('Enter location: ')

url = serviceurl + urllib.parse.urlencode({'address': address})

print('Retrieving', url)
uh = urllib.request.urlopen(url)

data = uh.read().decode()

print('Retrieved', len(data), 'characters')
js = json.loads(data)

place_id = js["results"][0]["place_id"]

print("Place id", place_id)

"""
OutPut:-
=========================
Enter location: Georgetown University Law Center
Retrieving http://py4e-data.dr-chuck.net/geojson?address=Georgetown+University+Law+Center
Retrieved 2019 characters
Place id ChIJzRC3Ga6Hs4kRYhWPTMBbXww
===================================================
"""



