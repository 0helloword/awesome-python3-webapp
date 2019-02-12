# -*- coding: utf-8 -*-

import MySQLdb.connector
# 注意把password设为你的root口令:
conn = mysql.connector.connect(user='wwwdata', password='wwwdata', database='awesome')
cursor = conn.cursor()
# 创建user表:
cursor.execute('create table cyj (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into cyj (id, name) values (%s, %s)', ['1', 'Michael'])
print (cursor.rowcount)
