import psycopg2
conn = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='1234')

cur = conn.cursor()

# getting version
print("postgreSQL database version: ")
cur.execute('SELECT version()')
print(cur.fetchone())

#checking table present
try:
    cur.execute('SELECT * FROM point_table')
except:
    print('table does not exit')
