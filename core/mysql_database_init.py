
from mysql.connector import cursor

TABLE = {}

TABLE['shields'] = "CREATE TABLE shields(" \
                   "mac CHAR(17) PRIMARY KEY," \
                   "nome VARCHAR(50) NOT NULL," \
                   "ip VARCHAR(200) NOT NULL," \
                   "port INTEGER NOT NULL);"

TABLE['pins'] = "CREATE TABLE pins(" \
                "mac_shield CHAR(17)," \
                "numero INTEGER," \
                "tipo CHAR(1) NOT NULL," \
                "nome VARCHAR(50) NOT NULL," \
                "usato VARCHAR(3) NOT NULL," \
                "out_mode VARCHAR(10)," \
                "in_mode VARCHAR(2)," \
                "PRIMARY KEY(mac_shield, numero)," \
                "FOREIGN KEY (mac_shield) REFERENCES shields(mac) " \
                "ON UPDATE CASCADE " \
                "ON DELETE CASCADE);"


import mysql.connector
def create_database(cursor, db_name):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(db_name))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

def create_table_shields(cursor):
    try:
        cursor.execute(TABLE['shields'])
    except mysql.connector.Error as err:
        print("Failed creating table shields: {}".format(err))
        exit(1)

def create_table_pins(cursor):
    try:
        cursor.execute(TABLE['pins'])
    except mysql.connector.Error as err:
        print("Failed creating table pins: {}".format(err))
        exit(1)