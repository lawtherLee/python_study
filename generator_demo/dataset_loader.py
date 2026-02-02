# 训练模型的时候 不是一次性喂给大批量的数据，而是分批次来训练的
import math


def dataset_loader(batch_size):
    """
    从原始文件读取所有数据，然后按照指定条数，生成每批次的数据
    :param: batch_size 每批次的数据条数
    :return: 生成器对象
    """
    with open("jaychou_lyrics.txt", "r", encoding="utf-8") as src_f:
        data_lines = [line.strip() for line in src_f.readlines()]
        data_lines = [line for line in data_lines if line]

    line_count = len(data_lines)

    # 计算批次数
    batch_count = math.ceil(line_count / batch_size)

    for batch_id in range(batch_count):
        yield data_lines[batch_id * batch_size : batch_id * batch_size + batch_size]
    # return (
    #     data_lines[batch_id * batch_size : batch_id * batch_size + batch_size]
    #     for batch_id in range(batch_count)
    # )


if __name__ == "__main__":
    my_g = dataset_loader(8)

    for batch_value in my_g:
        print(batch_value)
