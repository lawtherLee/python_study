import time
import multiprocessing


def coding(name, num):
    for i in range(num):
        print(f"{name}正在编写第{ i}行代码...")
        time.sleep(0.2)


def music(name, num):
    for i in range(num):
        print(f"{name}正在听第{ i}首音乐...")
        time.sleep(0.2)


p1 = multiprocessing.Process(target=coding, name="胡歌", args=("小王", 100))
p2 = multiprocessing.Process(
    target=music, name="刘亦菲", kwargs={"num": 100, "name": "小孙"}
)

if __name__ == "__main__":
    p1.start()
    p2.start()
