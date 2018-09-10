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

#database =  peewee.SqliteDatabase("QR_code.db")
database = peewee.MySQLDatabase(host = "192.168.110.55" , port = 3306 , user = "mkdc" , password = "MKDC123" , database = "converter_hsg")


class BaseModel(peewee.Model):
    class Meta:
        database = database

class dec_engraving(BaseModel):
    str_code = peewee.CharField(max_length = 20 ,  primary_key = True ,null = False , unique = True)
    code_from_die_casting = peewee.CharField(max_length = 26  ,null = False)
    code_from_probe = peewee.CharField(max_length = 20  ,null = True)
    code_engraved = peewee.BooleanField(index=True , null = True , default = 0 , unique = False )
    status = peewee.BooleanField(index=True , null = False , unique = False )
    date_added = peewee.DateTimeField(default = datetime.datetime.now , unique = True)



if __name__ == '__main__':

    database.create_tables([dec_engraving])
