def quick_sort(arr, start, end):
    """
    快速排序
    找分界值，小于分界值的放左边 大于放右边
    递归分界值两边的数据分别进行排序
    """
    if start >= end:
        return None
    # 边界值
    left = start
    right = end
    # 分界值
    pivot = arr[start]
    while left < right:
        # 右指针
        while arr[right] >= pivot and left < right:
            right -= 1
        arr[left] = arr[right]
        # 左指针
        while arr[left] <= pivot and left < right:
            left += 1
        arr[right] = arr[left]

    arr[left] = pivot
    quick_sort(arr, start, left - 1)
    quick_sort(arr, left + 1, end)

    return arr


if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5, 6]
    arr2 = [5, 2, 4, 6, 1, 3, -20]
    # print(quick_sort(arr1, 0, len(arr1) - 1))
    print(quick_sort(arr2, 0, len(arr2) - 1))
