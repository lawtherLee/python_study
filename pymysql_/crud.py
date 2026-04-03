import pymysql
from pymysql.cursors import DictCursor

DB_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "passwd": "123456",
    "database": "temp_test",
    "charset": "utf8",
    "cursorclass": DictCursor,
}


def get_db_connection():
    return pymysql.connect(**DB_CONFIG)


def 新增():
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            sql = "INSERT INTO users(username, password) VALUES(%s, %s)"
            res = cursor.execute(sql, ("小王", 18))
            if res > 0:
                conn.commit()
                print("新增成功")
            else:
                conn.rollback()
                print("新增失败")


def 删除():
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            sql = "DELETE FROM users WHERE id = %s"
            res = cursor.execute(sql, (3,))
            if res > 0:
                print("删除成功")
                conn.commit()
            else:
                print("删除失败")


def 修改():
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            sql = "UPDATE users SET username = %s WHERE id = %s"
            res = cursor.execute(sql, ("时鹏", 3))
            if res > 0:
                print("修改成功")
                conn.commit()
            else:
                print("修改失败")


def 查询():
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM users;")
            result = cursor.fetchall()
            for row in result:
                print(row)


if __name__ == "__main__":
    # 新增()
    # 修改()
    删除()
    查询()
