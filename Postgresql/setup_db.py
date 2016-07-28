#!/usr/bin/python
# -*- coding: utf-8 -*-
#setup postgresql db for data delete request


import psycopg2
import sys
import config
import csv
from datetime import datetime


def get_list(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        try:
            f_list = []
            for row in reader:
                if row:
                    f_list.append([str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5])])
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
    #print f_list
    return f_list


def main(filename):
    try:
        conn = psycopg2.connect(config.Params.conn_string)
        cur = conn.cursor()
        cur.execute(open("schema.sql", "r").read())
        #with conn:
        #    with conn.cursor() as curs:
        #        curs.execute(open("schema.sql", "r").read())
        #conn.commit()
        cur.execute("""SELECT table_schema,table_name
                         FROM information_schema.tables
                         WHERE table_schema = 'public'
                         ORDER BY table_schema,table_name;""")
        print('============================')
        print('table names:')
        for item in cur.fetchall():
            print('     ', item[1])
            print('============================')

        rows = get_list(filename)
        for r in rows:
            if r:
                update_time = datetime.strptime(r[5], '%m/%d/%y %H:%M')
                cur.execute("INSERT INTO ddrequest ( ESN, DDStatus, AccountId, Requestor, updated) \
                            VALUES (%s, %s, %s, %s, %s);", ( r[1], r[2], r[3], r[4], update_time))

        cur.execute("SELECT * FROM ddrequest ORDER by updated ASC;")
        print('sample data delete record')
        for item in cur.fetchall():
            print(item[0], item[1], item[2], item[3], item[4], item[5])

    except psycopg2.DatabaseError as e:
        print('Error %s' % e)
        sys.exit(1)
    except:
        print("Unexpected error:", sys.exc_info()[0])

    finally:
        conn.commit()
        cur.close()
        conn.close()


if __name__ == "__main__":
    main('fake_data.csv')
