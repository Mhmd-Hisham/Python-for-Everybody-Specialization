#!/usr/bin/env python3
# Instructor: Dr. Chuck Severance
# Course: Using Python to Access Web Data, University of Michigan, Coursera.

from urllib.request import urlopen
from bs4 import BeautifulSoup


url = "http://py4e-data.dr-chuck.net/comments_42.html" # Sample
htmlpage = urlopen(url).read()
    
soup = BeautifulSoup(htmlpage, "html.parser")
    
print(sum(int(tag.contents[0]) for tag in soup("span")))

