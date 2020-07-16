import sqlite3

conn=sqlite3.connect('database.bd')

#creating a cursor
c=conn.cursor()
#create a table



c.execute("SELECT rowid, * FROM customer ORDER BY first_name")

items=c.fetchall()


for item in items:
    print(item)

# these are data types
# NULL
# INTEGER
# real
# BLOB-stores as it is
# text

#commiting our command
conn.commit()


#close the connection
conn.close()





