import sqlite3

#Create the connection object

conn=sqlite3.connect("iii.db")

print("Opened the database successfully")

def create_table():
    conn.execute(''' CREATE TABLE SITE
                 (
                 SITECODE TEXT NOT NULL,
                 TIER TEXT NOT NULL,
                 External_ip CHAR(50),
                 Internal_ip CHAR(50));''')
    print("Table created successfully")

def insert_into_table(sitecode,tier,ext_ip,int_ip):
    conn.execute("INSERT INTO SITE (SITECODE,TIER,External_ip,Internal_ip) \
    VALUES ('%s','%s','%s','%s')" % (sitecode,tier,ext_ip, int_ip) );
    conn.commit()
    conn.close()

def query_table():
    pass
#Put in queries to database here

#Commit the changes to the database

#insert_into_table()
