import time
from student import Student


class StudentCms(object):
    def __init__(self):
        self.student_list = []

    @staticmethod
    def show_view():
        print("*" * 30)
        print("\t\t欢迎来到学生管理系统")
        print("\t\t1. 添加学生")
        print("\t\t2. 修改学生")
        print("\t\t3. 删除学生")
        print("\t\t4. 查询学生")
        print("\t\t5. 显示所有学生")
        print("\t\t0. 退出系统")
        print("*" * 30)

    def add_student(self):
        name = input("请输入学生姓名：")
        age = int(input("请输入学生年龄："))
        gender = input("请输入学生性别：")
        mobile = input("请输入学生手机号：")
        desc = input("请输入学生描述：")
        stu = Student(name, gender, age, mobile, desc)
        self.student_list.append(stu)
        print("添加学生信息成功")

    def update_student(self):
        update_name = input("请输入要修改的姓名：")
        for stu in self.student_list:
            if stu.name == update_name:
                stu.name = input("请输入学生姓名：")
                stu.age = int(input("请输入学生年龄："))
                stu.gender = input("请输入学生性别：")
                stu.mobile = input("请输入学生手机号：")
                stu.desc = input("请输入学生描述：")
                print("修改成功")
                return
        print("没有该学生")

    def delete_student(self):
        pass

    def search_student(self):
        pass

    def show_all_student(self):
        if len(self.student_list) == 0:
            print("暂无数据")
        for stu in self.student_list:
            print(stu)
        print()

    def save_student(self):
        pass

    def load_student(self):
        pass

    def start(self):
        self.load_student()
        while True:
            time.sleep(1)
            self.show_view()

            choice = input("请输入您的选择：")
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.update_student()
            elif choice == "3":
                self.delete_student()
            elif choice == "4":
                self.search_student()
            elif choice == "5":
                self.show_all_student()
            elif choice == "0":
                res = input("确定要退出系统吗？y/n")
                if res.lower() == "y":
                    print("欢迎下次再来")
                    break
            else:
                print("输入错误，请重新输入")


if __name__ == "__main__":
    stu1 = StudentCms()
    stu1.start()
