def insert_sort(arr):
    """
    插入排序
    把列表变成有序（第一个元素）无序两部分（从第二个元素开始）
    从无序列表中获取每个元素，插入到有序列表
    适合少量的数组
    """
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            else:
                break
    return arr


if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5, 6]
    arr2 = [5, 2, 4, 6, 1, 3]
    print(insert_sort(arr2))
