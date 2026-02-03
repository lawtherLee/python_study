class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average(self):
        if not self.scores:
            return 0

        total = sum(self.scores.values())
        av = total / len(self.scores)
        return round(av, 2)


class Class:
    def __init__(self, class_name):
        self.students = []
        self.class_name = class_name

    def add_stu(self, stu):
        if isinstance(stu, Student):
            self.students.append(stu)
            print(f"已添加学生：{stu.name}")
        else:
            print("只能添加Student类型对象")

    def del_stu(self, name):
        for stu in self.students:
            if stu.name == name:
                self.students.remove(stu)
                print(f"已删除学生：{stu.name}")
                return
        print("没有此学生")

    def update_stu(self, name, subject, new_score):
        for stu in self.students:
            if stu.name == name:
                if subject in stu.scores:
                    stu.scores[subject] = new_score
                    print(f"已更新学生：{stu.name}的{subject}成绩为：{new_score}")
                    return
                else:
                    print(f"没有此学生：{stu.name}的{subject}成绩")
                    return
        print("没有此学生")

    def query_stu(self, name):
        for stu in self.students:
            if stu.name == name:
                return stu
        print("查不到该学生")
        return None

    def get_subject_average(self, subject):
        total = 0
        count = 0
        for stu in self.students:
            if subject in stu.scores:
                total += stu.scores[subject]
                count += 1
        if count == 0:
            return 0
        av = total / count
        return round(av, 2)


# ----------------------------不依赖类实现---------------------------------


# --------------------------
# 功能1：学生相关操作
# --------------------------
def calculate_average(scores):
    """计算单个学生的平均分（保留两位小数）"""
    if not scores:
        return 0.0
    total = sum(scores.values())
    avg = total / len(scores)
    return round(avg, 2)


# --------------------------
# 功能2：班级相关操作
# --------------------------
def create_class(class_name):
    """创建一个班级（用字典表示）"""
    return {"class_name": class_name, "students": []}  # 学生列表，每个学生是一个字典


def add_student(class_info, student_name, scores):
    """添加学生到班级"""
    student = {"name": student_name, "scores": scores}
    class_info["students"].append(student)
    print(f"已添加学生：{student_name}")


def remove_student(class_info, student_name):
    """根据姓名删除学生"""
    for student in class_info["students"]:
        if student["name"] == student_name:
            class_info["students"].remove(student)
            print(f"已删除学生：{student_name}")
            return
    print(f"未找到学生：{student_name}")


def update_score(class_info, student_name, subject, new_score):
    """修改学生某科成绩"""
    for student in class_info["students"]:
        if student["name"] == student_name:
            if subject in student["scores"]:
                student["scores"][subject] = new_score
                print(f"已修改 {student_name} 的 {subject} 成绩为 {new_score}")
            else:
                print(f"{student_name} 没有 {subject} 这门科目")
            return
    print(f"未找到学生：{student_name}")


def find_student(class_info, student_name):
    """根据姓名查找学生"""
    for student in class_info["students"]:
        if student["name"] == student_name:
            return student
    return None


def get_subject_average(class_info, subject):
    """计算全班某科的平均分"""
    total = 0
    count = 0
    for student in class_info["students"]:
        if subject in student["scores"]:
            total += student["scores"][subject]
            count += 1
    if count == 0:
        return 0.0
    return round(total / count, 2)


if __name__ == "__main__":
    s1 = Student("张三", {"chinese": 80, "english": 90, "math": 100})
    print(s1.average())
    print("-" * 200)

    python_class = Class("Python 进阶班")

    # 创建学生对象
    alice = Student("Alice", {"math": 92, "english": 88, "science": 95})
    bob = Student("Bob", {"math": 78, "english": 80})
    charlie = Student("Charlie", {"math": 85, "english": 90, "science": 88})

    # 添加学生
    python_class.add_stu(alice)
    python_class.add_stu(bob)
    python_class.add_stu(charlie)

    # 通过班级查询
    found = python_class.query_stu("Alice")
    if found:
        print(f"找到学生：{found.name}，平均分：{found.average()}")

    # 更新学生成绩
    print(f"Bob的math成绩为：{python_class.query_stu('Bob').scores['math']}")
    python_class.update_stu("Bob", "math", 82)
    print(f"Bob的math成绩为：{python_class.query_stu('Bob').scores['math']}")

    # 删除学生
    found = python_class.query_stu("Charlie")
    print(f"找到学生：{found.name}")
    python_class.del_stu("Charlie")
    found = python_class.query_stu("Charlie")

    # 全班平均分
    math_avg = python_class.get_subject_average("math")
    print(f"全班数学平均分：{math_avg}")

    print("-" * 30 + "不依赖类实现" + "-" * 100)

    # 创建班级
    python_class = create_class("Python 进阶班")

    # 添加学生
    add_student(python_class, "Alice", {"math": 92, "english": 88, "science": 95})
    add_student(python_class, "Bob", {"math": 78, "english": 80})
    add_student(python_class, "Charlie", {"math": 85, "english": 90, "science": 88})

    # 查找学生并计算平均分
    alice = find_student(python_class, "Alice")
    if alice:
        avg = calculate_average(alice["scores"])
        print(f"找到学生：{alice['name']}，平均分：{avg}")

    # 修改成绩
    update_score(python_class, "Bob", "math", 82)

    # 删除学生
    remove_student(python_class, "Charlie")

    # 统计单科平均分
    math_avg = get_subject_average(python_class, "math")
    print(f"全班数学平均分：{math_avg}")
