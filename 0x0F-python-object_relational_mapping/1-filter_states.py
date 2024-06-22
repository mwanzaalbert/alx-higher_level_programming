#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Filter states.

A script that filters all states from the database hbtn_0e_0_usa that starst by
given search letter.
"""
import sys
import MySQLdb


def get_database_arguments():
    """
    Retrieve database connection arguments from the command line.

    Returns_:
        tuple_: A tuple containing the username, password, and database name.
               If any argument is missing, it returns None for that argument.
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
    return MySQLdb.connect(
        host="localhost",
        port=3306,
        user=usr,
        passwd=pwd,
        db=dbase,
    )


def fetch_and_print_states(cursor):
    """
    Execute query to fetch all states with names starting with 'N' from dbase.

    and Prints each row.

    Args_:
        cursor (MySQLdb.cursors.Cursor): The cursor object to execute the SQL
        query.
    """
    query = "SELECT * FROM states WHERE name is NOT  NULL AND name LIKE \
        'N%' ORDER BY id ASC"
    cursor.execute(query)
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)


def main():
    """Entry point of program to execute the database operations."""
    usr, pwd, dbase = get_database_arguments()
    msg = "Please provide the required arguments: username, password, and \
        database name."
    if not all([usr, pwd, dbase]):
        print(msg)
        sys.exit(1)

    conn = connect_to_database(usr, pwd, dbase)
    cur = conn.cursor()

    fetch_and_print_states(cur)

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
