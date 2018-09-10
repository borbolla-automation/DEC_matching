import csv, pyodbc

# set up some constants
MDB = 'C:\LeakDataManager\DataDB.mdb'; DRV = '{Microsoft Access Driver (*.mdb)}';
PWD = 'pw'

# connect to db
con = pyodbc.connect('DRIVER={};DBQ={};PWD={}'.format(DRV,MDB,PWD))
cur = con.cursor()

# run a query and get the results
SQL = 'SELECT * FROM mytable;' # your query goes here
rows = cur.execute(SQL).fetchall()
cur.close()
con.close()
