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

#database =  peewee.SqliteDatabase("QR_code2.db")
database = peewee.MySQLDatabase(host = "192.168.110.55" , port = 3306 , user = "mkdc" , password = "MKDC123" , database = "converter_hsg")

class BaseModel(peewee.Model):
    class Meta:
        database = database

class CastingCode(BaseModel):
    casting_code = peewee.CharField(max_length = 30  ,null = False , unique = True)
    code_engraved = peewee.BooleanField(index=True , null = True , default = 0 , unique = False )
    status = peewee.BooleanField(index=True , null = True , unique = False )
    line = peewee.CharField(max_length = 2 , null = False , default = 'J')
    date_added = peewee.DateTimeField(default = datetime.datetime.now )
    
class Machine(BaseModel):
    name = peewee.CharField(max_length = 6  ,null = False , unique = True )
    date_added = peewee.DateTimeField(default = datetime.datetime.now )

class CastingMachineLink(BaseModel):
    casting_code = peewee.ForeignKeyField(CastingCode)
    machine = peewee.ForeignKeyField(Machine)

class ManufacturingCode(BaseModel):
    casting_info = peewee.ForeignKeyField(CastingCode , primary_key = True , backref = 'manufacturing_code')
    manufacturing_code = peewee.CharField(max_length = 30  ,null = False)
    date_added = peewee.DateTimeField(default = datetime.datetime.now )

class Parameter(BaseModel):
    machine = peewee.ForeignKeyField(Machine  , null = False , backref = 'parameters')
    piece   = peewee.ForeignKeyField(CastingCode , null = False , backref = 'parameters')
    parameter_1   = peewee.FloatField(null = True)
    parameter_2   = peewee.FloatField(null = True)
    parameter_3   = peewee.FloatField(null = True)
    parameter_4   = peewee.FloatField(null = True)
    parameter_5   = peewee.FloatField(null = True)
    parameter_6   = peewee.FloatField(null = True)
    parameter_7   = peewee.FloatField(null = True)
    parameter_8   = peewee.FloatField(null = True)
    parameter_9   = peewee.FloatField(null = True)
    parameter_10  = peewee.FloatField(null = True)
    parameter_11  = peewee.FloatField(null = True)
    parameter_12  = peewee.FloatField(null = True)
    parameter_13  = peewee.FloatField(null = True)
    parameter_14  = peewee.FloatField(null = True)
    parameter_15  = peewee.FloatField(null = True)
    parameter_16  = peewee.FloatField(null = True)
    parameter_17  = peewee.FloatField(null = True)
    parameter_18  = peewee.FloatField(null = True)
    parameter_19  = peewee.FloatField(null = True)
    parameter_20  = peewee.FloatField(null = True)
    date_added    = peewee.DateTimeField(default = datetime.datetime.now )

def populate():
    casting_codes = ["KD06014G210180809000200002" , "KD06014G210180809000200003" , "KD06014G210180809000200004" , "KD06014G210180809000200005" , "KD06014G210180809000200006"]
    manufacturing_codes = ["4G210K180910D0001J0000" , "4G210K180910D0002J0000" , "4G210K180910D0003J0000" , "4G210K180910D0004K0000" , "4G210K180910D0005L0000"]
    machines = ["LKT1" , "LKT2"]

    parameters = [1 , 0 , 25.6984 , 854.6987]
    for code in casting_codes:
        CastingCode.get_or_create(casting_code = code)

    for mach in machines:
        Machine.get_or_create(name = mach)    

    machine1 = Machine.get(name = machines[0])
    machine2 = Machine.get(name = machines[1])

    casting_codes_obj = [CastingCode.get(casting_code = casting_codes[0]) , CastingCode.get(casting_code = casting_codes[1]) , CastingCode.get(casting_code = casting_codes[2]) , CastingCode.get(casting_code = casting_codes[3]) , CastingCode.get(casting_code = casting_codes[4])] 

    i=0
    for code in casting_codes_obj:
        ManufacturingCode.create(casting_info = code , manufacturing_code = manufacturing_codes[i])
        i+=1

    CastingMachineLink.create(casting_code = casting_codes_obj[0] , machine = machine1)
    CastingMachineLink.create(casting_code = casting_codes_obj[1] , machine = machine1)
    CastingMachineLink.create(casting_code = casting_codes_obj[2] , machine = machine1)
    CastingMachineLink.create(casting_code = casting_codes_obj[3] , machine = machine2)
    CastingMachineLink.create(casting_code = casting_codes_obj[4] , machine = machine2)

    Parameter.create(machine = machine1 , piece = casting_codes_obj[0] , parameter_1 = 0 , parameter_2 = 1 , parameter_3 = 452.369)
    Parameter.create(machine = machine1 , piece = casting_codes_obj[1] , parameter_1 = 1 , parameter_2 = 1 , parameter_3 = 451.369)
    Parameter.create(machine = machine1 , piece = casting_codes_obj[2] , parameter_1 = 0 , parameter_2 = 1 , parameter_3 = 450.369)
    Parameter.create(machine = machine2 , piece = casting_codes_obj[3] , parameter_1 = 1 , parameter_2 = 1 , parameter_3 = 459.369)
    Parameter.create(machine = machine2 , piece = casting_codes_obj[4] , parameter_1 = 0 , parameter_2 = 1 , parameter_3   = 458.369)

    








if __name__ == '__main__':

    database.create_tables([CastingCode  , Machine , CastingMachineLink , ManufacturingCode , Parameter])
    populate()

