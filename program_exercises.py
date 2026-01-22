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
        print(f"{j} * {i} = {i * j}", end=' ')
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
        if a ** 2 + b ** 2 == c ** 2:  # 0.14秒
            print(f"a={a},b={b},c={c}")

end_time = time()

print(f"执行时长： {(end_time - start_time):.2f}秒")
