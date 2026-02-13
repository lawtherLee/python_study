# 折半查找
#   列表必须有序
def binary_search(arr, target) -> bool:
    n = len(arr)
    if n == 0:
        return False
    mid = n // 2
    if arr[mid] == target:
        return True
    elif target < arr[mid]:
        return binary_search(arr[:mid], target)
    else:
        return binary_search(arr[mid + 1 :], target)


if __name__ == "__main__":
    test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(binary_search(test_numbers, 5))
