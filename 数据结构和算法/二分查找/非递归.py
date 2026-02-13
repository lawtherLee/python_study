def binary_search(arr, target) -> bool:
    # 边界值
    start = 0
    end = len(arr) - 1
    # 中间值

    while start <= end:
        mid = (start + end) // 2

        if target == arr[mid]:
            return True
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return False


if __name__ == "__main__":
    test_numbers = [1, 3, 5, 7, 9, 12, 15, 18, 21, 25]

    print(binary_search(test_numbers, 5))
