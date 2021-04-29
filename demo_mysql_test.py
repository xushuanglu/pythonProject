
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="runoob_db"
)

mycursor = mydb.cursor()

#创建数据库
# mycursor.execute("CREATE DATABASE runoob_db")


#输出数据库列表
# mycursor.execute("SHOW DATABASES")
#
# for x in mycursor:
#     print(x)

#创建表
# mycursor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")


#主键设置
# mycursor.execute("ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")


# sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
# val = ("RUNOOB", "https://www.runoob.com")
# mycursor.execute(sql, val)
#
# mydb.commit()  # 数据表内容有更新，必须使用到该语句
#
# print(mycursor.rowcount, "记录插入成功。")


#插入多条数据
# sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
# val = [
#     ('Google', 'https://www.google.com'),
#     ('Github', 'https://www.github.com'),
#     ('Taobao', 'https://www.taobao.com'),
#     ('stackoverflow', 'https://www.stackoverflow.com/')
# ]


# mycursor.executemany(sql, val)
#
# mydb.commit()  # 数据表内容有更新，必须使用到该语句
#
# print(mycursor.rowcount, "记录插入成功。")

#查询数据
mycursor.execute("SELECT * FROM sites")

myresult = mycursor.fetchall()  # fetchall() 获取所有记录

for x in myresult:
    print(x)