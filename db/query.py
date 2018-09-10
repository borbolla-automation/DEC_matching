import peewee
from models import *

import csv, pyodbc

class AccessDB(object):
    """docstring for AccessDB
"""
    def __init__(self, drive):
        
        self.drive = drive
        self.MDB = '%s:\DataManager\DataDB.mdb'%self.drive 
        print(self.MDB)
        self.DRV = '{Microsoft Access Driver (*.mdb)}'
        self.con = pyodbc.connect('DRIVER={};DBQ={}'.format(self.DRV,self.MDB))
        self.cur = self.con.cursor()

    def query(self):
        SQL = 'SELECT CodeData , Dtime FROM LeakTesterData WHERE Date()= DateValue(Dtime) OR Date()-1 = DateValue(Dtime);'
        self.rows = self.cur.execute(SQL).fetchall()
        print(len(self.rows))
        return self.rows

    def create_str(self):
        str_mtx = []
        for piece in self.rows:
            model = piece[0][6:11]
            factory = "K"
            datetime = piece[0][11:-3]
            serial   = piece[-3:] 
            str_mtx.append("%s%s%s%s"%(model , factory , datetime , serial))

        return str_mtx    


    def open_connctions(self):
        self.MDB = '%s:\DataManager\DataDB.mdb'%self.drive 
        self.DRV = '{Microsoft Access Driver (*.mdb)}'
        self.con = pyodbc.connect('DRIVER={};DBQ={}'.format(self.DRV,self.MDB))
        self.cur = con.cursor()

    def close_connections(self):
        self.cur.close()
        self.con.close()
        
"""
    def insert(self):
        for piece in self.rows:
            piece , created = dec_engraving.get_or_create(piece[])
"""




# set up some constants



# connect to db



# run a query and get the results
 # your query goes here
