class merge_sort(list):
    def sort(list):
        mid = len(list)//2
        l = list[:mid]
        r = list[mid:]

        merge_sort(l)
        merge_sort(r)

        i = j = k =0
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                list[k] = l[i]
                i += 1
            else:
                list[k] = r[j]
                j += 1
            k += 1

            while i < len(l):
                list[k] = l[i]
                i += 1
                k += 1
 
            while j < len(r):
                list[k] = r[j]
                j += 1
                k += 1

def printList(list):
    for i in range(len(list)):
        print(list[i], end=" ")
    print()

if __name__ == '__main__':
    list = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(list)
    merge_sort(list)
    print("Sorted array is: ", end="\n")
    printList(list)
