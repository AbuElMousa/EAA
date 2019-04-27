import sqlite3
import time

conn = sqlite3.connect("../eaa/db.sqlite3")
c = conn.cursor()

c.execute('''INSERT INTO sounds_sound VALUES ''' + str((4, 2, 69, 10, 10)))
conn.commit()
conn.close()
