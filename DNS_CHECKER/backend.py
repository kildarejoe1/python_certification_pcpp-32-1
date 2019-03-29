import sqlite3

def connect():
    conn=sqlite3.connect("III.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS SITES (sitecode TEXT, tier TEXT, external_ip TEXT, internal_ip TEXT )")
    conn.commit()
    conn.close()

#Create CRUD interface to insert,update,retrieve and delete data in the database.
def insert_data(sitecode,tier,external_ip,internal_ip):
    conn=sqlite3.connect("III.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO SITES VALUES ('%s','%s','%s','%s')" % (sitecode,tier,external_ip,internal_ip))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("III.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM SITES")
    row=cur.fetchall()
    conn.close()
    return row

def search(sitecode=""):
    conn=sqlite3.connect("III.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM SITES WHERE sitecode='%s'" % sitecode )
    row=cur.fetchall()
    conn.close()
    return row
