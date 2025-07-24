def selection_sort(li):
    n = len(li)
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if li[j] < li[min]:
                min = j
        li[i],li[min] = li[min],li[i]

    return li

my_list =[8,5,3,9,1,6,2,0]
print(selection_sort(my_list))