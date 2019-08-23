# coding: utf-8

import cgi 
import pymysql.cursors
import json
dbConection = pymysql.connect(host='localhost',
                             user='root',
                             db='projet_lettrine',
                             cursorclass=pymysql.cursors.DictCursor)

print("Content-type: application/json; charset=utf-8\n")




with dbConection.cursor() as cursor:

    sql = "SELECT * FROM automate"

    cursor.execute(sql)
    result_set = cursor.fetchall()
    print(result_set)