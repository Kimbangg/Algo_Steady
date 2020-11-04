def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list)//2
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])
    return merge(left,right)
 
def merge(left, right):
    result = []
    while len(left) > 0 or len(right)>0:
        if len(left) > 0 and len(right) > 0:
 
            if left[0] <= right[0]:
                result.append(left[0])
                left=left[1:]
            else:
                result.append(right[0])
                right = right[1:]
 
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result
 
 
list = [69, 10, 30, 2, 16, 8, 31, 22]
 
print(merge_sort(list))
