import sqlite3

def initialise_db():
    conn=sqlite3.connect("gui_dns.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS gui (sitecode TEXT, tier TEXT, external_ip TEXT, internal_ip TEXT )")
    conn.commit()
    conn.close()

def insert_data(sitecode,tier,external_ip,internal_ip):
    conn=sqlite3.connect("gui_dns.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO gui VALUES ('%s','%s','%s','%s')" % (sitecode,tier,external_ip,internal_ip))
    conn.commit()
    conn.close()

initialise_db()
insert_data("site1","app","1.2.3.4","2.3.4.5")
