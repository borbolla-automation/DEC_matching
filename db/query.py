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
        self.str_dc_mtx = []
        for piece in self.rows:
            print(piece[0])
            if 'MASTER' not in piece[0]:
                model = piece[0][6:11]
                factory = "K"
                datetime = piece[0][11:-3]
                serial   = piece[0][-3:] 
                self.str_dc_mtx.append(["%s%s%s%s"%(model , factory , datetime , serial),piece[0]])
                

        return self.str_mtx , self.dc_mtx    

    def insert(self):
        i = 0
        for code in self.str_mtx:
            try:
                piece , created = dec_engraving.get_or_create(str_code = code , code_from_die_casting = self.dc_mtx[i] , status = 0)
                i += 1
            except peewee.IntegrityError as error:
                raise error

            



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
