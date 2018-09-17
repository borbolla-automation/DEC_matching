import peewee
from models2 import *
import datetime
from uuid import getnode as get_mac
import csv, pyodbc

class AccessDB(object):
    """docstring for AccessDB
"""
    def __init__(self):
        
        self.computer_id = {'LEAK TEST #1': 268891672818713 , 'LEAK TEST #2' : 84440845556379}
        self.mac = get_mac()
        if self.mac == self.computer_id['LEAK TEST #1']:
            self.drive = 'C'
            print('LEAK TEST #1')
        if self.mac == self.computer_id['LEAK TEST #2']:
            self.drive = 'D'    
            print('LEAK TEST #2')
        
        self.MDB = '%s:\LeakDataManager\DataDB.mdb'%self.drive 
        print(self.MDB)
        self.DRV = '{Microsoft Access Driver (*.mdb)}'
        self.con = pyodbc.connect('DRIVER={};DBQ={}'.format(self.DRV,self.MDB))
        self.cur = self.con.cursor()
        

    def query(self):
        SQL = 'SELECT  CodeData , Dtime ,Num , TotalOkNg   FROM LeakTesterData WHERE Date()= DateValue(Dtime) OR Date()-1 = DateValue(Dtime) ORDER BY Num DESC;'
        self.rows = self.cur.execute(SQL).fetchall()
        print(len(self.rows))
        return self.rows[-1]

    def insert(self):
        
        casting_piece , created = CastingCode.get_or_create(casting_code = self.rows[0][0] ,)

        if self.mac == self.computer_id['LEAK TEST #1']:
            machine = Machine.get(name = "LKT1")

        if self.mac == self.computer_id['LEAK TEST #2']:
            machine = Machine.get(name = "LKT2")

        cml,cml_created = CastingMachineLink.get_or_create(casting_code = casting_piece , machine = machine)
        parameters,p_created = Parameter.get_or_create(machine = machine , piece = casting_piece , parameter_1 = self.rows[0][3])

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
    leak2 = AccessDB()
    last = leak2.query()
    #crt_str = leak2.create_str()
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
