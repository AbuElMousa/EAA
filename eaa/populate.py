import sqlite3

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

'''
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = c.fetchall()
print(tables)
'''

c.execute("INSERT INTO configuration_configuration VALUES (1, 1, 'blah', 100, 0, 0, 'blah')")

conn.commit()
conn.close()
