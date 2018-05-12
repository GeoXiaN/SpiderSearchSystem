#!/usr/bin/env python3
import sqlite3

# Connect to SQLite3
conn = sqlite3.connect('websites.db')

c = conn.cursor()

# Create database tables if they don't exist yet
c.execute('''CREATE TABLE IF NOT EXISTS sites (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    url TEXT,
    last_updated DATETIME,
    last_scanned DATETIME
)''')

c.execute('''CREATE TABLE IF NOT EXISTS keywords (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sites_id_fk INTEGER,
    keyword TEXT
)''')

c.execute('''CREATE TABLE IF NOT EXISTS links_to (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sites_id_fk INTEGER,
    linked_sites_id_fk INTEGER
)''')

# Pull a database of sites to scrape
for row in c.execute('SELECT * FROM sites'):
    print(row)


# Scrape them one by one

# Use BeautifulSoup to parse for more links and database

# Gets links and save them to database

# Save changes to database
conn.commit()

# Close connection
conn.close()

# Write information to JSON files for ZeroNet to read
