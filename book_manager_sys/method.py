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


def add_info() -> None:
    # 如果没有图书数据，则设置编号从1开始
    new_id = max([book["编号"] for book in books]) + 1 if books else 1
    name = input("请输入图书名称：").strip()
    price1 = input("请输入图书价格: ").strip()
    # 价格默认0
    price = float(price1) if price1 else 0
    was_lend = input("请输入图书出租状态【是/否】: ").strip()
    status = 1 if was_lend == "是" else 0

    new_book = {
        "编号": new_id,
        "书名": name,
        "价格": price,
        "出租状态": status,
    }
    books.append(new_book)

    print(f"书籍《{name}》添加成功！")


def delete_info() -> None:
    """根据编号删除书籍"""
    try:
        book_id = int(input("请输入要删除的图书编号："))
        for book in books:
            if book["编号"] == book_id:
                if book["出租状态"]:
                    print(f"《{book['书名']}》正在出租中，无法删除")
                    return
                books.remove(book)
                print(f"编号{book_id}的书籍已删除！")
                return
        print(f"编号{book_id}的图书不存在")
    except ValueError:
        print("输入的编号有误")
        return


def update_info() -> None:
    """修改书籍信息"""
    try:
        book_id = int(input("请输入要修改的图书编号："))
        for book in books:
            if book["编号"] == book_id:
                print(
                    f"当前书籍信息：书名={book['书名']}，价格={book['价格']}，出租状态={book['出租状态']}"
                )
                new_name = input("请输入新的图书名称：").strip()
                if new_name:
                    book["书名"] = new_name
                    print(f"书名已更新为：{new_name}")
                new_price = input("请输入新的图书价格：").strip()
                if new_price:
                    try:
                        new_price_float = float(new_price)
                        if new_price_float < 0:
                            print("价格不能小于0")
                        else:
                            book["价格"] = new_price_float
                            print(f"价格已更新为：{new_price_float}")
                    except ValueError:
                        print("输入的图书价格有误")
                new_status = input("请输入新的图书出租状态【是/否】：").strip()
                if new_status:
                    status = 1 if new_status == "是" else 0
                    book["出租状态"] = status
                    print(f"出租状态已更新为：{new_status}")

                print(f"\n编号{book_id}的书籍信息修改完成！")
                return
        print(f"编号{book_id}的图书不存在")
    except ValueError:
        print("输入的编号有误")
        return


def search_info() -> None:
    name = input("请输入要查询的图书名称：").strip()
    for book in books:
        if book["书名"] == name:
            print(
                f"编号：{book['编号']}，书名：{book['书名']}，价格：{book['价格']}，出租状态：{book['出租状态']}"
            )
            return
    print(f"图书《{name}》不存在")


def search_all_info() -> None:
    if not books:
        print("暂无数据")
        return
    print("\n===== 所有书籍信息 =====")
    for book in books:
        price = float(book["价格"])
        print(
            f"编号：{book['编号']}，书名：{book['书名']}，价格：{price:.2f}，出租状态：{'已出租' if book['出租状态'] else '未出租'}"
        )
    print("=======================")


if __name__ == "__main__":
    read_book_file()
