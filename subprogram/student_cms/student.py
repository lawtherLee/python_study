class Student(object):
    def __init__(self, name, gender, age, mobile, desc):
        self.name = name
        self.age = age
        self.gender = gender
        self.mobile = mobile
        self.desc = desc

    def __str__(self):
        return f"""
    姓名：{self.name}
    性别：{self.gender}
    年龄：{self.age}
    手机：{self.mobile}
    描述：{self.desc}"""


if __name__ == "__main__":
    s1 = Student("乔峰", "男", 18, "13888888888", "小乔")
    print(s1)
