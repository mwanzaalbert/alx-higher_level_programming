#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Get all states.

A script that lists all states from the database hbtn_0e_0_usa.
"""
import sys
import MySQLdb


def get_database_arguments():
    """
    Retrieve database connection arguments from the command line.

    Returns_:
        tuple: containing the username, password, and database name.
               If any arg is missing, it returns None for that arg.
    """
    if len(sys.argv) >= 4:
        usr = sys.argv[1]
        pwd = sys.argv[2]
        dbase = sys.argv[3]

    return usr, pwd, dbase


def connect_to_database(usr, pwd, dbase):
    """
    Establish a connection to the MySQL database.

    Args_:
        usr (str): The username for the database connection.
        pwd (str): The password for the database connection.
        dbase (str): The name of the database to connect to.

    Returns_:
        MySQLdb.Connection: A connection object to the MySQL database.
    """
    return MySQLdb.connect(host="localhost", port=3306, user=usr, passwd=pwd,
                           db=dbase)


def fetch_and_print_states(cursor):
    """
    Execute query to fetch all states from the database and print each row.

    Args_:
        cursor (MySQLdb.cursors.Cursor): The cursor object to execute the
        SQL query.
    """
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)


def main():
    """Entry point of program to execute the database operations."""
    usr, pwd, dbase = get_database_arguments()
    msg = "Please provide the required arguments: username, password, and"
    if not all([usr, pwd, dbase]):
        print(f"{msg} database name.")
        sys.exit(1)

    conn = connect_to_database(usr, pwd, dbase)
    cur = conn.cursor()

    fetch_and_print_states(cur)

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()


# conn = MySQLdb.connect(host="localhost", port=3306,
#                        user=usr, passwd=pwd, db=dbase, charset="utf8")
# cur = conn.cursor()
# # HERE I have to know SQL to grab all states in my database
# cur.execute("SELECT * FROM states ORDER BY id ASC")
# query_rows = cur.fetchall()
# for row in query_rows:
#     print(row)
# cur.close()
# conn.close()
