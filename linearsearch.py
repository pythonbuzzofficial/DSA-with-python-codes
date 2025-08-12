def linear_search(li,target):
    for i in range(len(li)):
        if li[i] == target:
            return i
    return -1
        
my_list = [6,3,2,4,7,9]
target = 10
result = linear_search(my_list,target)

if result!=-1:
    print(f"Target element found at index {result}")
else:
    print("Target element not found")


