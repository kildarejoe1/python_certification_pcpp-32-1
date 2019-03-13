
import sqlite3

#Create the connection object

conn=sqlite3.connect("sqlite_practice.db")

print("Opened the database successfully")

def create_table():
    conn.execute(''' CREATE TABLE COMPANY
                 (ID INT PRIMARY KEY NOT NULL,
                 NAME TEXT NOT NULL,
                 AGE INT NOT NULL,
                 ADDRESS CHAR(50),
                 SALARY REAL);''')
    print("Table created successfully")

def insert_into_table():
    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
    VALUES (1, 'PAUL', 32, ' Calafornia', 20000.00)");
    conn.commit()

def query_table():
    cursor=conn.execute("SELECT id,name,address,salary from COMPANY")
    for row in cursor:
        print "ID = ", row[0]
        print "NAME = ", row[1]
        print "ADDRESS = ", row[2]
        print "SALARY = ", row[3]
#Put in queries to database here

#Commit the changes to the database

#insert_into_table()
query_table()


conn.close()
print("Closing the connection")
#Close the database connection.
