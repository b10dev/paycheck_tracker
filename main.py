"""
Author: B10 Devs
Description:
    This is the main.py file for the paycheck tracker program.
    Associated Files:
        Utility.py
        SqliteConnector.py
        MysqlConnector.py
        paycheckClass.py
        paychecks.db
        READ ME.txt
"""
from Utility import Utility

if __name__ == '__main__':

    print("\n_________________Paycheck Tracker____________v 3.0")
    print(""" 
    _________________________________________________
    |   (\(\                                          |
    |  =(^.^)=                           Date______   |
    |  (")_(")                                        |   
    |                                     $_________  |  
    | ____________________________________Dollars     |
    |                                                 | 
    | Memo:__________             Sign:____________   |  
    | |:000000000   |:00000000       |:0000           |
    |_________________________________________________|\n""")

    Utility.start_of_program()


