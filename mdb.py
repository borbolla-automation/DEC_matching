import csv, pyodbc

# set up some constants
MDB = 'C:\LeakDataManager\DataDB.mdb'; DRV = '{Microsoft Access Driver (*.mdb)}';


# connect to db
con = pyodbc.connect('DRIVER={};DBQ={}'.format(DRV,MDB))
cur = con.cursor()

# run a query and get the results
SQL = 'SELECT Num ,Dtime FROM LeakTesterData ORDER BY Num DESC;' # your query goes here
rows = cur.execute(SQL).fetchall()
print(rows[-50:])
cur.close()
con.close()
