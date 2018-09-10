import peewee
from models import *
import datetime

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
        return self.rows[-1]

    def create_str(self):
        self.str_dc_mtx = []
        dt = datetime.datetime.now()
        for piece in self.rows[-1]:
            print(piece[0])
            if 'MASTER' not in piece[0]:
                model = piece[0][6:11]
                yy = str(dt.year)[2:]
                mm = str(dt.month).zfill(2)
                dd = str(dt.day).zfill(2)   
                date = "%s%s%s"%(yy,mm,dd)
                hh = dt.hour
                if hh > 5 and hh <19:
                    shift = 'D'
                else:
                    shift = 'N'
                serial   = piece[0][-3:].zfill(4) 
                self.str_dc_mtx.append(["%s%s%s%s"%(model , date , shift , serial),piece[0]])
                

        return self.str_dc_mtx    

    def insert(self):
        for code in self.str_dc_mtx:
            print(code)
            piece , created = dec_engraving.get_or_create(str_code = code[0] , code_from_die_casting = code[1] , status = 0)
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
        
"""
    def insert(self):
        for piece in self.rows:
            piece , created = dec_engraving.get_or_create(piece[])
"""




# set up some constants



# connect to db



# run a query and get the results
 # your query goes here
