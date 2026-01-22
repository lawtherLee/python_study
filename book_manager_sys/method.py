# 存储所有图书信息的列表
books = []

# 预设管理员账号密码
ADMIN_USER = "admin"
ADMIN_PWD = "123456"


def read_book_file() -> None:
    """
    从文件中读取图书信息
    """
    try:
        with open("book.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            # 该方法遍历列表中的元素，并返回索引和元素本身 0 书名、价格、状态···
            for idx, line in enumerate(lines):
                # strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
                print(idx, line.strip())
                # 检测是否有空行
                if not line:
                    continue
                name, price, status = line.split(",")
                book = {
                    "编号": idx + 1,
                    "书名": name,
                    "价格": price,
                    "出租状态": bool(int(status)),  # 0→False(未租), 1→True(已租)
                }
                books.append(book)
                print("图书数据加载完成")
    except FileNotFoundError:
        print("文件不存在，系统将以空数据启动")


def admin_login() -> bool:
    for _ in range(3):
        username = input("请输入管理员账号：")
        password = input("请输入管理员密码：")
        if username == ADMIN_USER and password == ADMIN_PWD:
            print("登录成功")
            return True
        else:
            print("登录失败,请重试")
    print("错误次数达上限，已锁定")
    return False


def print_info():
    print("\n===== 蓝天社区图书馆管理系统 =====")
    print("1: 添加书籍(书籍编号，书籍名，书籍价格，书籍出租状态【是/否】)")
    print("2: 删除书籍(根据编号删除)")
    print("3: 修改书籍信息(只能改书籍名，书籍出租状态)")
    print("4: 查询单个书籍信息(根据书籍名查)")
    print("5: 查询所有书籍信息")
    print("6: 退出系统")
    print("================================")


if __name__ == "__main__":
    read_book_file()
