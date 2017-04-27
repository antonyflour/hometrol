import mysql.connector


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

TABLE['events'] = "CREATE TABLE events(" \
                "id VARCHAR(50) PRIMARY KEY," \
                "repetition_interval INTEGER," \
                "enabled BOOLEAN," \
                "last_exec_time DATETIME);"

TABLE['conditions'] = "CREATE TABLE conditions(" \
                "id VARCHAR(50) PRIMARY KEY," \
                "event VARCHAR(50) NOT NULL," \
                "type VARCHAR(50) NOT NULL," \
                "mac_shield CHAR(17)," \
                "pin_number INTEGER," \
                "expected_state INTEGER," \
                "FOREIGN KEY (mac_shield) REFERENCES shields(mac)," \
                "FOREIGN KEY (event) REFERENCES events(id) " \
                "ON UPDATE CASCADE " \
                "ON DELETE CASCADE);"

TABLE['actions'] = "CREATE TABLE actions(" \
                "id VARCHAR(50) PRIMARY KEY," \
                "event VARCHAR(50) NOT NULL," \
                "type VARCHAR(50) NOT NULL," \
                "mac_shield CHAR(17)," \
                "pin_number INTEGER," \
                "state INTEGER," \
                "email VARCHAR(100)," \
                "msg VARCHAR(1000)," \
                "FOREIGN KEY (mac_shield) REFERENCES shields(mac)," \
                "FOREIGN KEY (event) REFERENCES events(id) " \
                "ON UPDATE CASCADE " \
                "ON DELETE CASCADE);"

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

def create_table_events(cursor):
    try:
        cursor.execute(TABLE['events'])
    except mysql.connector.Error as err:
        print("Failed creating table pins: {}".format(err))
        exit(1)

def create_table_conditions(cursor):
    try:
        cursor.execute(TABLE['conditions'])
    except mysql.connector.Error as err:
        print("Failed creating table pins: {}".format(err))
        exit(1)

def create_table_actions(cursor):
    try:
        cursor.execute(TABLE['actions'])
    except mysql.connector.Error as err:
        print("Failed creating table pins: {}".format(err))
        exit(1)