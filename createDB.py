# create a database table in sqlite
import sqlite3
conn=sqlite3.connect('music.db')
cur=conn.cursor()
cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks (title TEXT,plays INTEGER)')
conn.close()
