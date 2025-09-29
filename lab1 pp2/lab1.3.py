def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

lst = [4, 2, 5, 1]
insertion_sort(lst)
print(lst)  # [1, 2, 4, 5]
