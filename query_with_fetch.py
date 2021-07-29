# Python program to connect to mysql using

# Importing packages
from mysql.connector import MySQLConnection, Error
from mysql_connect import read_db_config


def query_with_fetchone():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute('Select * from world.country')

        row = cursor.fetchone()

        while row is not None:
            print(row)
            row = cursor.fetchone()


    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()


# Query with fetchall
def query_with_fetechall():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute('Select * from world.country')
        rows = cursor.fetchall()

        # Printing total number of rows
        print("Total Row(s):", cursor.rowcount)

        for row in rows:
            print(row)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


# Generator that chunks database call into many series of fetchmany calls
def row_iter(cursor, size=10):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        else:
            for row in rows:
                yield row


# Fetch with many example
def query_with_fetchwithmany():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * from world.city")

        for row in row_iter(cursor, 10):
            print(row)

    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':

    choice = int(input("Enter your choice\n "
                       "1:Query_with_fetchone\n "
                       "2:Query_with_fetechall\n "
                       "3:Query_with_fetchmany\n"))

    if choice == 1:
        query_with_fetchone()
    elif choice == 2:
        query_with_fetechall()
    elif choice == 3:
        query_with_fetchwithmany()
    else:
        print("Wrong Choice!!")
