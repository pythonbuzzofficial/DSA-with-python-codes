def quick_sort(li,start,end):

    if start < end :

        pivot = li[end]
        i = start - 1
        for j in range(start,end):
            if li[j] <=pivot:
                i+=1
                li[i],li[j] = li[j],li[i]
        
        li[i+1],li[end] = li[end],li[i+1]
        pivot_index = i+1
        
        quick_sort(li,start,pivot_index-1)
        quick_sort(li,pivot_index+1,end)


my_list = [35,20,40,55,10,30]
quick_sort(my_list,0,len(my_list)-1)
print(my_list)