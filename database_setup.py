#!/usr/bin/env python3
import psycopg2
import json
import sys
from psycopg2.extras import RealDictCursor
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def create_db():
    con = psycopg2.connect(dbname='postgres')
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    cur = con.cursor()
    cur.execute("CREATE DATABASE EXCHANGE_RATES")
    con.commit()
    print("Database has been created")
    con.close()


def get_data(*qureies):
    ''' This function used to connect to the database'''
    try:
        con = psycopg2.connect(dbname="exchange_rates")
    except psycopg2.Error as e:
        print ("Unable to connect!")
        print (e.pgerror)
        print (e.diag.message_detail)
        sys.exit(1)
    else:
        cur = con.cursor()
        for qurey in qureies:
            cur.execute(qurey)
        try:
            d = cur.fetchall()
            return d
        except:
            pass

        con.close()


def connect_database(query):
    '''Connect to postgrelsql DB using psycopg2 DB-API '''
    try:
        con = psycopg2.connect(dbname="exchange_rates")
        cur = con.cursor()
        print(query)
        cur.execute(query)
        con.commit()
        print("The query has been excuted")
    except psycopg2.Error as e:
        print("Unable to connect!")
        # print the error message
        print(e.pgerror)
    else:
        con.close()


def insert_value(postgres_insert_query, record_to_insert):
    try:
        connection = psycopg2.connect(dbname="exchange_rates")
        cursor = connection.cursor()

        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into rate table")

    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to insert record into mobile table", error)

    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def create_exchange_table():
    '''Create a table '''
    # create_db()
    # unpack the header into the table values
    createTable = '''CREATE TABLE RATE(
                  id serial primary key,
                  date text,
                  source text,
                  target text,
                  value numeric);'''
    # connect to the database and run the query
    connect_database(createTable)


if __name__ == '__main__':
    create_exchange_table()
