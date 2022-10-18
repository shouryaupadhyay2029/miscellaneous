def insertion_sort(list):
    for i in range(0,len(list)):
        x = list[i]
        j = i-1
        while j and x < list[j]:
            list[j+1] = list[j]
            j = j-1
            list[j+1] = x
            
list = [31, 41, 59, 26, 41, 58]
insertion_sort(list)
print(list)