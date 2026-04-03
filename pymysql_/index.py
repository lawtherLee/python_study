import pymysql

with pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="123456",
    database="temp_test",
    charset="utf8",
) as connect:
    with connect.cursor() as cursor:
        cursor.execute("SHOW TABLES;")
        print("数据库中的表：", cursor.fetchall())
        cursor.execute("SELECT * FROM computers;")
        data = cursor.fetchall()
        for row in data:
            print(row)
