def insertion_sort(li):
     for i in range(1,len(li)):
          key = li[i]
          j = i-1      
          while j>=0 and li[j] > key:
               li[j+1] = li[j]
               j -=1
          li[j+1] = key
     return li
   
my_list = [6,4,1,8,5,2,7,0]
print(insertion_sort(my_list))
