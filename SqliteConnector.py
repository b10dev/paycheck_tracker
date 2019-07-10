"""
Author: B10 Devs
Description:
    This class contains all of the methods to use a sqlite database
    instead of a MySql Database.
"""
import sqlite3


class SqliteConnector:
    # :memory: used for debugging
    # connection = sqlite3.connect(":memory:")
    connection = sqlite3.connect("paychecks.db")
    cursor = connection.cursor()
    select_all_from_table = "SELECT * FROM paychecks"

    def __init__(self):
        pass

    @classmethod
    def close_cursor(cls):
        SqliteConnector.cursor.close()
        SqliteConnector.connection.close()
        # print("Debug: Connection and Cursor closed")

    # Commit the cursor after any command
    @classmethod
    def commit_cursor(cls):
        SqliteConnector.connection.commit()
        # print("Debug: Commit")

    # Make a simple query
    @classmethod
    def simple_query(cls, x):
        insert_command = x
        SqliteConnector.cursor.execute(insert_command)
        SqliteConnector.commit_cursor()
        # print("Debug: Simple query executed")

    @classmethod
    def create_table(cls):
        try:
            SqliteConnector.cursor.execute("""CREATE TABLE paychecks (
                                    date TEXT NOT NULL UNIQUE,
                                    gross REAL,
                                    our_cut REAL,
                                    workers_comp REAL,
                                    misc REAL,
                                    total REAL,
                                    notes TEXT
                                    )""")
            SqliteConnector.commit_cursor()
        except:
            print("Successfully connected to the Database!!")

        # print("Debug: Database creation")