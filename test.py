my_list = [1, 2, 3, 4, 5]


def reverse_list_by_yield(lst):
    for i in range(len(lst) - 1, -1, -1):
        yield lst[i]


if __name__ == "__main__":
    for i in reverse_list_by_yield(my_list):
        print(i)
