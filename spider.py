#!/usr/bin/env python3
import sqlite3
import json
# Connect to SQLite3
conn = sqlite3.connect('websites.db')

c = conn.cursor()

# Create database tables if they don't exist yet
c.execute('''CREATE TABLE IF NOT EXISTS sites (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    address TEXT,
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

# Pulling in the dictionary to kick start search database
addressbookFile = open('./zeronet/data/1Name2NXVi1RDPDgf5617UoW7xA6YrhM9F/data/names.json',"r")
addressbook = json.loads (addressbookFile.read())

for site_name in addressbook:
    site_address = addressbook[site_name]
    print(site_address)
    c.execute('SELECT * FROM sites WHERE address = ?', (site_address,))
    if not c.fetchone():
        c.execute("INSERT INTO sites VALUES (NULL,'',?,NULL,NULL)", (site_address,))


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
