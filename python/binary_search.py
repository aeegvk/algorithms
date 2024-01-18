def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    if target > arr[high] or target < arr[low]:
        return -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

if __name__ == '__main__':
    print(binary_search([1,2,3,4,5,6,7], 4))