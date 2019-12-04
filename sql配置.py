# @Time : 2019/11/1 9:26
# @Author : YLXY
# @File : sql配置.py
# -*- coding: utf-8 -*-

import pymssql

import pymssql
#sql服务器名，这里(127.0.0.1)是本地数据库IP
serverName = '127.0.0.1'
#登陆用户名和密码
userName = 'sa'
passWord = '123456'
#建立连接并获取cursor
conn = pymssql.connect(serverName , userName , passWord, "data")
cursor = conn.cursor()
# 创建测试表 persons，包含字段：ID、name、salesrep
cursor.execute("""
IF OBJECT_ID('persons', 'U') IS NOT NULL
    DROP TABLE persons
CREATE TABLE persons (
    id INT NOT NULL,
    name VARCHAR(100),
    salesrep VARCHAR(100),
    PRIMARY KEY(id)
)
""")
# 插入三条测试数据
cursor.executemany(
    "INSERT INTO persons VALUES (%d, %s, %s)",
    [(1, 'John Smith', 'John Doe'),
     (2, 'Jane Doe', 'Joe Dog'),
     (3, 'Mike T.', 'Sarah H.')])
# 如果连接时没有设置autocommit为True的话，必须主动调用commit() 来保存更改。
conn.commit()
# 查询记录
cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
# 获取一条记录
row = cursor.fetchone()
# 循环打印记录(这里只有一条，所以只打印出一条)
while row:
    print("ID=%d, Name=%s" % (row[0], row[1]))
    row = cursor.fetchone()
# 连接用完后记得关闭以释放资源
conn.close()
