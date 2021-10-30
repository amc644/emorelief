import sqlite3
from sqlite3 import Error

def connect():
    try:
        connection=sqlite3.connect('db/db.db')
        return connection
    except Error as error:
        print(error)
        return None

def executeSentence(_sql,parameters):
    try:
        connection=connect()
        if connection:
            cur=connection.cursor()
            rows=cur.execute(_sql,parameters).rowcount
            cur.close()
            connection.commit()
            connection.close()
            return rows
        else:
            print('The connection to the database could not be established. See errors.')
            return -1
    except Error as error:
        print('Error when executing SQL sentence '+str(error))
        return -1

def dictionaryMaker(cursor,row):
    dictionary={}
    for idx,col in enumerate(cursor.description):
        dictionary[col[0]]=row[idx]
    return dictionary

def select(_sql,parameters):
    try:
        connection=connect()
        if connection:
            connection.row_factory=dictionaryMaker 
            cur=connection.cursor()
            if parameters:
                cur.execute(_sql,parameters)
            else:
                cur.execute(_sql)
            rows=cur.fetchall()
            cur.close()
            connection.close()
            return rows
        else:
            print('The connection to the database could not be established. See errors.')
            return None
    except Error as error:
        print('Error when executing SQL sentence'+str(error))
        return None