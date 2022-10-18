def linear_search(list, target):

    for i in range(0, len(list)):
        if list[i] == target:
            return i

    return None

def verify(index):
    if index is not None:
        print("target found at index: ", index)
    else:
        print("target not found in list")

number = [1,2,3,4,5,6,7,8,9,10]
x = int(input("number you wanna search: "))
result = linear_search(number, x)
verify(result)