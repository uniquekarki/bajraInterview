import sqlite3
from prettytable import from_db_cursor

con = sqlite3.connect('bajra.db')
cur = con.cursor()

stringQuery = 'SELECT * FROM hospital'
cur.execute(stringQuery)
mytable = from_db_cursor(cur)
print('\nHospital Table')
print(mytable)