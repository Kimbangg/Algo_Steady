def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        # 최소값 찾는 처리
        for k in range(i+1, len(arr)):
            if arr[k] < arr[min_index]:
                min_index = k
        # 최소값의 위치를 바꿔주는 처리
        tmp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = tmp
    return arr
test = [12, 13, 11, 14, 10]
print(selection_sort(test))
