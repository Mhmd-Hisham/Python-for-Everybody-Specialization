#!/usr/bin/env python3
# Instructor: Dr. Chuck Severance
# Course: Using Python to Access Web Data, University of Michigan, Coursera.

from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_link(url, position):
    htmlpage = urlopen(url).read()
    soup = BeautifulSoup(htmlpage, "html.parser")
    return soup("a")[position].get("href", None)

url = input("Enter URL: ")
count = int(input("Enter count: "))
position = int(input("Enter position: "))-1

i = 0
print("Retrieving:", url)
while i < count:
    url = get_link(url, position)
    print("Retrieving:", url)

    i += 1

