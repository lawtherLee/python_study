# 统计字符串中，各个字符的个数，"hello world" 字符串统计的结果为： h:1 e:1 l:3 o:2 d:1 r:1
def get_dict():
    """
    牛
    :return:
    """
    str1 = "hello world"
    str_dist = {}
    for i in str1:
        if i not in str_dist:
            str_dist[i] = 1
        else:
            str_dist[i] += 1
    print(str_dist)
