#!/usr/bin/env python

"""
  ____   ____  _____  ____   ____  _      _                                _    _ _______ ____  __  __       _______ _____ ____  _   _ 
 |  _ \ / __ \|  __ \|  _ \ / __ \| |    | |        /\                /\  | |  | |__   __/ __ \|  \/  |   /\|__   __|_   _/ __ \| \ | |
 | |_) | |  | | |__) | |_) | |  | | |    | |       /  \              /  \ | |  | |  | | | |  | | \  / |  /  \  | |    | || |  | |  \| |
 |  _ <| |  | |  _  /|  _ <| |  | | |    | |      / /\ \            / /\ \| |  | |  | | | |  | | |\/| | / /\ \ | |    | || |  | | . ` |
 | |_) | |__| | | \ \| |_) | |__| | |____| |____ / ____ \          / ____ \ |__| |  | | | |__| | |  | |/ ____ \| |   _| || |__| | |\  |
 |____/ \____/|_|  \_\____/ \____/|______|______/_/    \_\        /_/    \_\____/   |_|  \____/|_|  |_/_/    \_\_|  |_____\____/|_| \_|
                                                                                                                                       
 +------------------------------------------------------------------------------------------------------------------------------------+
 |                                                                                                                                    |
 |  Module Name    : Models                                                                                                           |
 |  Module Purpose : Mysql Database Design , and model relationship , for database functioning                                        |
 |  Inputs  : ORM class                                                                                                               |
 |  Outputs : Create code , database Object                                                                                           |
 |  Author : Borbolla Automation Inc                                                                                                  |
 |  Email : ingenieria@borbolla-automation.com                                                                                        |
 |  webpage : www.borbolla-automation.com                                                                                             |
 +------------------------------------------------------------------------------------------------------------------------------------+
"""

import peewee
import datetime

database =  peewee.SqliteDatabase("QR_code.db")
#database = peewee.MySQLDatabase(host = "0.tcp.ngrok.io" , port = 17199 , user = "mkdc" , password = "MKDC123" , database = "converter_hsg")


class BaseModel(peewee.Model):
    class Meta:
        database = database

 

class CastingCode(BaseModel):
    #str_code = peewee.CharField(max_length = 20 ,  primary_key = True ,null = False , unique = True)
    casting_code = peewee.CharField(max_length = 26  ,null = False , unique = True)
    #code_from_probe = peewee.CharField(max_length = 20  ,null = True)
    code_engraved = peewee.BooleanField(index=True , null = True , default = 0 , unique = False )
    status = peewee.BooleanField(index=True , null = True , unique = False )
    #manufacturing_info = peewee.ForeignKeyField(ManufacturingCode , backref = 'casting_info')
    line = peewee.CharField(max_length = 2 , null = False , default = 'J')
    date_added = peewee.DateTimeField(default = datetime.datetime.now , unique = True)
    
class ManufacturingCode(BaseModel):
    #str_code = peewee.CharField(max_length = 20 ,  primary_key = True ,null = False , unique = True)
    manufacturing_code = peewee.CharField(max_length = 26  ,null = False)
    casting_info = peewee.ForeignKeyField(CastingCode , backref = 'manufacturing_info')
    date_added = peewee.DateTimeField(default = datetime.datetime.now , unique = True)

class Machine(BaseModel):
    name = peewee.CharField(max_length = 3  ,null = False , )
    casting_info = peewee.ForeignKeyField(CastingCode , backref = 'machines' , null = True)
    #manufacturing_info = peewee.ForeignKeyField(ManufacturingCode , backref = 'machines' , null = True)
    date_added = peewee.DateTimeField(default = datetime.datetime.now , unique = True)
   
class Parameter(BaseModel):
    #str_code = peewee.CharField(max_length = 20 ,  primary_key = True ,null = False , unique = True)
    machine = peewee.ForeignKeyField(Machine , backref = 'parameters')
    parameter_1  = peewee.FloatField()
    parameter_2  = peewee.FloatField()
    parameter_3  = peewee.FloatField()
    parameter_4  = peewee.FloatField()
    parameter_5  = peewee.FloatField()
    parameter_6  = peewee.FloatField()
    parameter_7  = peewee.FloatField()
    parameter_8  = peewee.FloatField()
    parameter_9  = peewee.FloatField()
    parameter_10 = peewee.FloatField()
    parameter_11  = peewee.FloatField()
    parameter_12  = peewee.FloatField()
    parameter_13  = peewee.FloatField()
    parameter_14  = peewee.FloatField()
    parameter_15  = peewee.FloatField()
    parameter_16  = peewee.FloatField()
    parameter_17  = peewee.FloatField()
    parameter_18  = peewee.FloatField()
    parameter_19  = peewee.FloatField()
    parameter_20 = peewee.FloatField()
    date_added = peewee.DateTimeField(default = datetime.datetime.now , unique = True)

if __name__ == '__main__':

    database.create_tables([CastingCode , ManufacturingCode , Machine , Parameter])


