#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psycopg2
import datetime
import config

ii = datetime.datetime.now().date()
conn = psycopg2.connect(config.Params.conn_string)

cur = conn.cursor()

cur.execute("SELECT * FROM ddrequest ORDER BY updated DESC LIMIT 1000;")
print('============================')
for item in cur.fetchall():
    print(item)
print('============================')

#cur.execute("DELETE FROM quote WHERE code_id=610;")
#
cur.execute("""SELECT table_schema,table_name
                  FROM information_schema.tables
                  WHERE table_schema = 'public'
                  ORDER BY table_schema,table_name;""")
for item in cur.fetchall():
    print(item[1])
 #print cur.execute
print('============================')
conn.commit()
cur.close()
conn.close()
