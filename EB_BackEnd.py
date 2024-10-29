#BackEnd
import sqlite3

def EBData():
    Connect=sqlite3.connect("EB.db")
    cur=Connect.cursor()
    cur.executescript('''
    CREATE TABLE IF NOT EXISTS EB(
       Id INTEGER PRIMARY KEY,
       Customer_ID TEXT,
       Customer_Name TEXT,
       Units_Consumed TEXT,
       Amount TEXT
    );
    ''')
    Connect.commit()
    Connect.close()

def CalculateEBRecord(CustomerID,CustomerName,UnitsConsumed):
    Connect=sqlite3.connect("EB.db")
    cur=Connect.cursor()
    UNITS=float(UnitsConsumed)
    if(UNITS > 0):
        if(UNITS <= 100):
            Amount = 100*1.00
        elif(UNITS > 100 and UNITS <= 200):
            Amount = 100*1.00+(UNITS-100)*2.50
        elif(UNITS > 200 and UNITS <= 500):
            Amount = 100*1.00+200*2.50+(UNITS-200)*4.00
        elif(UNITS > 500):
            Amount = 100*1.00+200*2.50+500*4.00+(UNITS-500)*6.00
    elif(UNITS == 0 or UNITS < 0):
        Amount = 0.00
    cur.execute('''INSERT INTO EB VALUES (NULL, ?, ?, ?, ? ) ''', ( CustomerID, CustomerName, UnitsConsumed, Amount) )
    Connect.commit()
    Connect.close()

def ViewEBData():
    Connect=sqlite3.connect("EB.db")
    cur=Connect.cursor()
    cur.execute("SELECT * FROM EB")
    rows=cur.fetchall()
    Connect.close()
    return rows

def DeleteEBRecord(id):
    Connect=sqlite3.connect("EB.db")
    cur=Connect.cursor()
    cur.execute("DELETE FROM EB WHERE id = ?", ( id, ) )
    Connect.commit()
    Connect.close()


def SearchEBData(CustomerID="",CustomerName=""):
    Connect=sqlite3.connect("EB.db")
    cur=Connect.cursor()
    cur.execute('''SELECT * FROM EB WHERE Customer_ID=? OR Customer_Name=? ''',( CustomerID, CustomerName ))
    rows=cur.fetchall()
    Connect.close()
    return rows

EBData()
