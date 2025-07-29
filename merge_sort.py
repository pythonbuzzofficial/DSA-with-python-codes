def merge_sort(li):
    if len(li)<=1:
        return li
    mid = len(li)//2
    left = merge_sort(li[:mid])
    right =merge_sort(li[mid:])

    sorted_list = []
    i = j = 0

    while i<len(left) and j <len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i+=1
        else:
            sorted_list.append(right[j])
            j+=1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list


my_list =[5,2,9,1,6,3]
print(merge_sort(my_list) )