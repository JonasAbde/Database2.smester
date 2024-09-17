#
# PostgreSQL test script for aiven postgreSQL connection
#
# To install psycopg connector
# python3 -m pip install psycopg2 (psycopg2-binary for mac)
#

import psycopg2

# Modify parameters to align your actual database settings
user = 'avnadmin'
password = 'AVNS_GEfpyamT7kd4de4fIwU'
host = 'pg-2f37e134-empire1266.f.aivencloud.com'
port = '19276'
database = 'defaultdb'
sslmode = 'sslmode=require'

# create URL connection string to connect your database
db_conn_str = 'postgres://' + user + ':' + password + '@' + host + ':' + port + '/' + database + '?' + sslmode


# test data connection
def test_conn():
    query_sql = 'SELECT VERSION()'
    cur = conn.cursor()

    try:
        cur.execute(query_sql)

        # Commit the changes
        conn.commit()
        print("Database connected succesfully")

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting", error)
        conn.rollback()

    finally:
        # Close the cursor and connection
        if cur:
            cur.close()


"""
Here starts the main program

"""


if __name__ == "__main__":
    conn = psycopg2.connect(db_conn_str)    # connect to database
    test_conn()                             # test connection
    conn.close()                            # close database connection
