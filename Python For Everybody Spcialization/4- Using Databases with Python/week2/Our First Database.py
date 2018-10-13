#!/usr/bin/env python3
# Instructor: Dr. Chuck Severance
# Using Databases with Python, University of Michigan, Coursera.


import sqlite3


conn = sqlite3.connect('firstdb.sqlite')
cur = conn.cursor()


cur.execute("CREATE TABLE IF NOT EXISTS Ages (name VARCHAR(128), age INTEGER)")
cur.execute("DELETE FROM Ages;")

cur.execute("INSERT INTO Ages (name, age) VALUES ('Chrismedi', 13);")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Arlo', 27);")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Sharleen', 15);")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Maisey', 37);")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Cadie', 22);")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Aishah', 37);")

cur.execute("SELECT hex(name || age) AS X FROM Ages ORDER BY X")

conn.commit()

first_row = cur.fetchone()

print(first_row)


cur.close()
