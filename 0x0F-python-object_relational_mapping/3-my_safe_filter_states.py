#!/usr/bin/python3
"""Script lists all states with a name starting with N from database
Takes three arguments:
    mysql username
    mysql password
    database name
Connects to default host (localhost) and port (3306)
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    if len(sys.argv) != 4:
        print("Usage: ./script_name.py <username> <password> <database_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    try:
        with MySQLdb.connect(user=username, passwd=password, db=db_name) as db:
            c = db.cursor()
            query = """SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"""
            c.execute(query)
            rows = c.fetchall()
            for row in rows:
                print(row)
    except MySQLdb.Error as e:
        print("Error:", e)
