def select_sort(arr):
    """
    选择排序
    每轮比较，都找到最小值所在的索引，然后和最小索引进行交换
    """
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5, 6]
    arr2 = [5, 2, 4, 6, 6, 1, 3]

    # print(select_sort(arr))
    print(select_sort(arr2))
