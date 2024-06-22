#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
All cities by state.

A script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa.
"""
import sys
import MySQLdb


def get_database_arguments():
    """
    Retrieve database connection arguments from the command line.

    Returns_:
        tuple: A tuple containing the username, password, database name, and
                the state name to search respectively.
               If any argument is missing, it returns None for that argument.
    """
    return sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]


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
        db=dbase
    )


def fetch_and_print_cities(cursor, state_name):
    """
    Execute a query to fetch all cities in the specified state from the dbase.

    and print each row in the required format.

    Args_:
        cursor (MySQLdb.cursors.Cursor): The cursor object to execute the query
        state_name (str): The name of the state to search for.
    """
    query = """SELECT cities.name FROM cities
    INNER JOIN states ON cities.state_id = states.id
    WHERE BINARY states.name=%s
    ORDER BY cities.id ASC
    """

    cursor.execute(query, (state_name,))
    query_rows = cursor.fetchall()
    
    print("")
    for index, row in enumerate(query_rows):
        if index < len(query_rows) - 1:
            print(row[0], end=", ")
        else:
            print(row[0], end="")
    

def main():
    """Entry point of program to execute the database operations."""
    usr, pwd, dbase, tosearch = get_database_arguments()
    if not all([usr, pwd, dbase, tosearch]):
        msg = "Please provide the required arguments: username, password, \
            database name, and state name to search."
        print(msg)
        sys.exit(1)

    conn = connect_to_database(usr, pwd, dbase)
    cur = conn.cursor()

    fetch_and_print_cities(cur, tosearch)

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
