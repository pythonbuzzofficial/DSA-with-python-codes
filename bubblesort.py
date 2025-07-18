def bubble_sort(li):
     n = len(li)
     for i in range(n):
          for j in range(n-1-i):
               if li[j] > li[j+1]:
                    li[j],li[j+1] = li[j+1],li[j]

     return li              

my_list = [40,20,120,130,30,50,10,80]
print(bubble_sort(my_list))