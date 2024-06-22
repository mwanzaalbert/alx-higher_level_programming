#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Cities by states.

A script that lists all cities from the database hbtn_0e_4_usa.
"""
import sys
import MySQLdb


def get_database_arguments():
    """
    Retrieve database connection arguments from the command line.

    Returns_:
        tuple: A tuple containing the username, password, and database name.
               If any argument is missing, it returns None for that argument.
    """
    db_args = sys.argv

    usr = db_args[1] if len(db_args) > 1 else None
    pwd = db_args[2] if len(db_args) > 2 else None
    dbase = db_args[3] if len(db_args) > 3 else None

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
        charset="utf8"
    )


def fetch_and_print_cities(cursor):
    """
    Execute a query to fetch all cities and their corresponding state names.

    from the database, and print each row.

    Args_:
        cursor (MySQLdb.cursors.Cursor): The cursor object to execute the query
    """
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC;
    """
    cursor.execute(query)
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)


def main():
    """Entry point of program to execute the database operations."""
    usr, pwd, dbase = get_database_arguments()
    if not all([usr, pwd, dbase]):
        msg = "Please provide the required arguments: username, password, and \
            database name."
        print(msg)
        sys.exit(1)

    conn = connect_to_database(usr, pwd, dbase)
    cur = conn.cursor()

    fetch_and_print_cities(cur)

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
