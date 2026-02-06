def bubble_sort(arr: list) -> list:
    """
    冒泡排序
    相邻元素两两比较，大的往后，这样第一轮比较完，最大值就在最大索引处
    """
    n = len(arr)
    for i in range(n - 1):
        count = 0
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                count += 1
        print(f"交换了{count}次")
        if count == 0:
            break
    return arr


if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5, 6]
    arr2 = [5, 2, 4, 6, 1, 3]
    print(bubble_sort([1, 2, 3, 4, 5]))
    print(bubble_sort([5, 3, 4, 7, 2]))
