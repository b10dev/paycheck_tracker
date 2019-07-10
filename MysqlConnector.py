"""
Author: B10 Devs
Description:
    This class Contains the methods and functions to switch from a sqlite
    database, to a MySql database.
"""
import mysql.connector


class MysqlConnector:
    connection = mysql.connector.connect(user='', password='', host='', database='paychecks')
    cursor = connection.cursor()
    select_all_from_table = "SELECT * FROM paychecks"

    def __init__(self):
        pass


    @classmethod
    def close_cursor(cls):
        MysqlConnector.cursor.close()
        MysqlConnector.connection.close()

    # Commit the cursor after any command
    @classmethod
    def commit_cursor(cls):
        MysqlConnector.connection.commit()

    # Make a simple query
    @classmethod
    def simple_query(cls, x):
        insert_command = x
        MysqlConnector.cursor.execute(insert_command)
        MysqlConnector.commit_cursor()

    @classmethod
    def create_table(cls):
        try:
            MysqlConnector.cursor.execute("""CREATE TABLE paychecks (
                                    date TEXT NOT NULL UNIQUE,
                                    gross REAL,
                                    our_cut REAL,
                                    workers_comp REAL,
                                    misc REAL,
                                    total REAL,
                                    notes TEXT
                                    )""")
            MysqlConnector.commit_cursor()
        except:
            print("Successfully connected to the Database!!")
