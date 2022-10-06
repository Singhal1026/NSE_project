# importing data from database
import psycopg2

hostname = 'localhost'
database = 'Bhav_copy'
username = 'postgres'
pwd = 'Sql@1234'
port_id = 5433
cur = None
conn = None

try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    )

    cur = conn.cursor()

    cur.execute("SELECT * FROM bhavcopy where symbol='20MICRONS'")
    print(cur.fetchall())


except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
