import sqlite3

#Create the connection object

conn=sqlite3.connect("sqlite_practice.file")

#Now create the cursor that will execute the sql queries

cursor=conn.cursor()

#Put in queries to database here

conn.commit()
#Commit the changes to the database
conn.close()
#Close the database connection.
