# Python program to connect to mysql using

# Importing packages
from mysql.connector import MySQLConnection, Error
from mysql_connect import read_db_config


# Connect to Mysql Database
def connect():
    db_config = read_db_config()
    conn = None
    try:
        print('Connecting to mysql database...')
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            print('Connection is established')
        else:
            print('Connection Failed.')
    except Error as error:
        print(error)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Connection closed.')


if __name__ == '__main__':
    connect()
