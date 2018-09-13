import peewee
from models import *
import datetime
import os
import csv, pyodbc

class AccessDB(object):
    """docstring for AccessDB
"""
    def __init__(self, drive):
        
        self.drive = drive
        self.MDB = '%s\DataDB.mdb'%os.getcwd()

        print(self.MDB)
        self.DRV = '{Microsoft Access Driver (*.mdb)}'
        self.con = pyodbc.connect('DRIVER={};DBQ={}'.format(self.DRV,self.MDB))
        self.cur = self.con.cursor()

    def query(self):
        SQL = 'SELECT  CodeData , Dtime ,Num FROM LeakTesterData WHERE Date()= DateValue(Dtime) OR Date()-1 = DateValue(Dtime) ORDER BY Num DESC;'
        self.rows = self.cur.execute(SQL).fetchall()
        print(len(self.rows))
        return self.rows[0]

    def create_str(self):
        self.str_dc_mtx = []
        dt = datetime.datetime.now()
        
        if 'MASTER' not in self.rows[0][0]:
            model = self.rows[0][0][6:11]
            yy = str(dt.year)[2:]
            mm = str(dt.month).zfill(2)
            dd = str(dt.day).zfill(2)   
            date = "%s%s%s"%(yy,mm,dd)
            hh = dt.hour
            if hh > 5 and hh <19:
                shift = 'D'
            else:
                shift = 'N'
            serial   = self.rows[0][0][-3:].zfill(4) 
            print(self.rows[0][0])
            self.str_dc_mtx = ["%s%s%s%s"%(model , date , shift , serial),self.rows[0][0]]
                

        return self.str_dc_mtx    

    def insert(self):
        
        print(self.str_dc_mtx)

        machine
        casting_piece , created = dec_engraving.get_or_create(casting_code = self.rows[0])
        if created : 
            print("Created") 
        else: 
            print("not created!")    
            
            



    def open_connctions(self):
        self.MDB = '%s:\DataManager\DataDB.mdb'%self.drive 
        self.DRV = '{Microsoft Access Driver (*.mdb)}'
        self.con = pyodbc.connect('DRIVER={};DBQ={}'.format(self.DRV,self.MDB))
        self.cur = con.cursor()

    def close_connections(self):
        self.cur.close()
        self.con.close()
        

if __name__ == '__main__':
    leak2 = AccessDB('D')
    last = leak2.query()
    crt_str = leak2.create_str()
    created = leak2.insert()
    leak2.close_connections()
"""
    def insert(self):
        for piece in self.rows:
            piece , created = dec_engraving.get_or_create(piece[])
"""




# set up some constants



# connect to db



# run a query and get the results
 # your query goes here
