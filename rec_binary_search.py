"""def rec_binary_search(list, target):

    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return rec_binary_search(list[midpoint+1:], target)
            else:
                return rec_binary_search(list[:midpoint], target)
def verify(index):
    if index is not False:
        print("Target found in the list: ", index)
    else:
        print("Target not found in list")

number = [1,2,3,4,5,6,7,8,9,10]
x = int(input("Number you wanna search: "))
result = rec_binary_search(number, x)
verify(result)"""




def binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        mid_point = (len(list))//2
        if list[mid_point] == target:
            return True
        else:
            if list[mid_point] > target:
                return binary_search(list[:mid_point], target)
            else:
                return binary_search(list[mid_point+1:], target)
    
def linear_search(list, target):
    for x in range(len(list)):
        if list[x] == target:
            return True
      
            
list = [1,2,3,4,5,8,7,4,5,7]
target = 7

search_binary = binary_search(list,target)
search_linear = linear_search(list,target)
if search_binary == True or search_linear == True:
    print(True)
else:
    print(False)


