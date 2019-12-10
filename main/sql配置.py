# @Time : 2019/11/1 9:26
# @Author : YLXY
# @File : sql配置.py
# -*- coding: utf-8 -*-

import pymysql as pms
score,length = 50,10
db = pms.connect('localhost', 'root', '2252', "greedy_snake")
cursor = db.cursor()
cursor.execute('insert into data1(score,length) values (%d,%d);'%(score,length))

cursor.close()
