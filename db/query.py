import peewee
from models import *
import datetime
from uuid import getnode as get_mac
import csv, pyodbc

class AccessDB(object):
    """docstring for AccessDB
"""
    def __init__(self, drive):
        
        self.computer_id = {'LEAK TEST #1': 268891672818713 , 'LEAK TEST #2' : 84440845556379}
        self.mac = get_mac()
        if self.mac == self.computer_id['LEAK TEST #1']:
            self.drive = 'C'
        if self.mac == self.computer_id['LEAK TEST #2']:
            self.drive = 'D'    
        
        self.MDB = '%s:\DataManager\DataDB.mdb'%self.drive 
        print(self.MDB)
        self.DRV = '{Microsoft Access Driver (*.mdb)}'
        self.con = pyodbc.connect('DRIVER={};DBQ={}'.format(self.DRV,self.MDB))
        self.cur = self.con.cursor()
        

    def query(self):
        SQL = 'SELECT  CodeData , Dtime ,Num FROM LeakTesterData WHERE Date()= DateValue(Dtime) OR Date()-1 = DateValue(Dtime) ORDER BY Num DESC;'
        self.rows = self.cur.execute(SQL).fetchall()
        print(len(self.rows))
        return self.rows[-1]

    def insert(self):
        
        print(self.str_dc_mtx)
        if self.mac == self.computer_id['LEAK TEST #1']:
            machine , created = machine.get_or_create(name = 'LEAK TEST #1' )
        if self.mac == self.computer_id['LEAK TEST #2']:
            machine , created = machine.get_or_create(name = 'LEAK TEST #2' )    
        
        casting_piece , created = dec_engraving.get_or_create(casting_code = self.rows[0][0])
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
