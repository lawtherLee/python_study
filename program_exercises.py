from time import *

# 需求: 数字金字塔
# 即: 打印一个由数字组成的金字塔，共n层。例如，当n = 5
# 时，输出为：
#      1
#     121
#    12321
#   1234321
#  123454321

n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(i):
        print(j + 1, end="")
    for j in range(i - 2, -1, -1):
        print(j + 1, end="")
    print()

# 需求: 输出乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} * {i} = {i * j}", end=" ")
    print(" ")

# 基础的算法调优
start_time = time()

# for a in range(1001):
#     for b in range(1001):
#         for c in range(1001):
#             if a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000:  # 108秒
#             if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:  # 58秒
#                 print(f"a={a},b={b},c={c}")


for a in range(1001):
    for b in range(1001):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:  # 0.14秒
            print(f"a={a},b={b},c={c}")

end_time = time()

print(f"执行时长： {(end_time - start_time):.2f}秒")


# 定义函数findall，要求返回符合要求的所有位置的起始下标，
# 如字符串"helloworldhellopythonhelloc++hellojava"
# 需要找出里面所有的"hello"的位置，返回的格式是一个元组，即：(0,10,21,29)
def findall(s, target):
    return tuple(
        i for i in range(len(s) - len(target) + 1) if s[i : i + len(target)] == target
    )


result = findall("helloworldhellopythonhelloc++hellojava", "hello")
print(result)


def fun(*args):
    """
    计算传入参数的总和
    参数可以是列表或字典的任意组合
    如果是列表，则计算列表元素的总和
    如果是字典，则计算字典值的总和
    """
    total = 0
    for i in args:
        if isinstance(i, list):
            total += sum(i)
        else:
            total += sum(i.values())
    return total


str1 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_qrcode(str1):
    """
    获取4位数验证码
    :param str1:
    :return:
    """
    verify_code = random.choices(str1, k=4)
    qrcode = "".join(verify_code)
    return qrcode


print(get_qrcode(str1))
