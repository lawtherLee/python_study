# 需求：水仙花数（Narcissistic number）
# 是指一个n位数（n≥3），其各位数字的n次幂之和等于该数本身‌。
# 例如，153是一个水仙花数，因为153=1^3+5^3+3^3。
# ‌计算100~999之间的水仙花数。
print("100~999之间的水仙花数有：")
for num in range(100, 1000):
    hundred = num // 100
    ten = (num // 10) % 10
    unit = num % 10
    sum_of_cubes = hundred ** 3 + ten ** 3 + unit ** 3
    if sum_of_cubes == num:
        print(f"{num} = {hundred}³ + {ten}³ + {unit}³ = {hundred ** 3} + {ten ** 3} + {unit ** 3}")

# 约瑟夫环
# 需求：有一天你穿越到了古代, 碰巧约到古代的皇帝在杀人, 有两个消息, 1个好消息, 1个坏消息.
# 坏消息: 你也在此列.
# 好消息: 你可以选择自己占的位置.
# 规则: 让所有的人从1开始不断数数, 每次累加1, 只要数到3的倍数, 就干掉这个人,
# 直至剩下最后1个人, 他站的位置就是: 幸运数字.
# 参考答案：10个人玩游戏 -> 幸运数字: 4
n = int(input("请输入人数："))
list_of_people = [i for i in range(1, n + 1)]
current_num = 0
i = 0
while len(list_of_people) != 1:
    current_num += 1
    if current_num % 3 == 0:
        del list_of_people[i]
        i -= 1
    i += 1
    if i >= len(list_of_people):
        i = 0
print(f"{n}人参与游戏，幸运数字是{list_of_people[0]}")
