import csv, pyodbc

# set up some constants
MDB = 'C:\LeakDataManager\DataDB.mdb'; DRV = '{Microsoft Access Driver (*.mdb)}';


# connect to db
con = pyodbc.connect('DRIVER={};DBQ={}'.format(DRV,MDB))
cur = con.cursor()

# run a query and get the results
SQL = 'SELECT * FROM LeakTesterData WHERE Num = 43411;' # your query goes here
rows = cur.execute(SQL).fetchall()
print(rows[-1])
cur.close()
con.close()
