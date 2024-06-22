#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filter states by user input.

A script that filters all states from the database hbtn_0e_0_usa by given
search argument.
"""
import sys
import MySQLdb


def get_database_arguments():
    """
    Retrieve database connection arguments from the command line.

    Returns_:
        tuple: A tuple containing the username, password, database name, and
               the state name to search. If any argument is missing, it Returns
               None for that argument.
    """
    db_args = sys.argv

    usr = db_args[1] if len(db_args) > 1 else None
    pwd = db_args[2] if len(db_args) > 2 else None
    dbase = db_args[3] if len(db_args) > 3 else None
    to_search = db_args[4] if len(db_args) > 4 else None

    return usr, pwd, dbase, to_search


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


def fetch_and_print_state(cursor, to_search):
    """
    Execute query to fetch the state with the specified name from the dbase.

    and print each row.

    Args_:
        cursor (MySQLdb.cursors.Cursor): The cursor object to execute the
                query.
        to_search (str): The name of the state to search for.
    """
    query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC" % (
        to_search,)
    cursor.execute(query)
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)


def main():
    """Entry point of program to execute the database operations."""
    usr, pwd, dbase, to_search = get_database_arguments()
    if not all([usr, pwd, dbase, to_search]):
        msg = "Please provide the required arguments: username, password, \
            database name, and state name to search."
        print(msg)
        sys.exit(1)

    conn = connect_to_database(usr, pwd, dbase)
    cur = conn.cursor()

    fetch_and_print_state(cur, to_search)

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()


#!/usr/bin/env python3

# db_args = sys.argv

# if len(db_args) > 1:
#     usr = sys.argv[1]
# if len(db_args) > 2:
#     pwd = sys.argv[2]
# if len(db_args) > 3:
#     dbase = sys.argv[3]
# if len(db_args) > 4:
#     to_search = sys.argv[4]


# conn = MySQLdb.connect(host="localhost", port=3306,
#                        user=usr, passwd=pwd, db=dbase, charset="utf8")
# cur = conn.cursor()
# # Using f-string format
# cur.execute(f"SELECT * FROM states WHERE name='{to_search}' ORDER BY id ASC")
# # cur.execute("SELECT * FROM states WHERE name='%s' ORDER BY id ASC" % to_search) # using format specifier
# query_rows = cur.fetchall()
# for row in query_rows:
#     print(row)
# cur.close()
# conn.close()
