#!/usr/bin/python3
"""Script lists all states with a name starting with N from database
Takes three arguments:
    mysql username
    mysql password
    database name
Connects to default host (localhost) and port (3306)
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    username = argv[1]
    password = argv[2]
    db_name = argv[3]

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
