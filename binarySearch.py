def binary_search(li,target):
    low = 0
    high = len(li)-1

    while low<=high:
         mid = (low+high)//2

         if li[mid] == target:
              return mid
         elif li[mid]<target:
              low = mid+1
         else:
              high =mid-1
    return -1    
              

my_list = [2,4,6,8,10,12,14]
target =15
result = binary_search(my_list,target)

if result!=-1:
     print(f"Target element found at index {result}")
else:
     print("Target element not found")
