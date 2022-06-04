import psycopg2

def Connection():
    conn = psycopg2.connect(
        host='localhost',
        database='ipldb',
        user='postgres',
        password='1234')
    return conn

conn = Connection()
