"""###array = [
   [1, 2, 3],
   [4, 5, 6],
   [7, 8, 9]
]"""

#1D array
"""def find_sum(array):
    total = 0
    for i in range(len(array)):
        total = total+i
    return total

x = find_sum(array)
print(x)"""

#2D array

"""def find_sum(array):
    total = 0
    for row in range(len(array)):
        total = total + row
        for col in range(len(array)):
            total = total + col 
    return total...............
x = find_sum(array)
print(x)"""


"""
x = int(input("Factorial of > "))
def factoril(n):
    if n == 0:
        return 1
    else:
        return fib(n-1) + fib(n-2)
""" 

"""x = int(input("Factorial of > "))
def fib(n):
    if n==0:
        return 0
    if n == 1 or n ==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(x))"""

# makeing a linkedlist
class node:
    def __init__(self,data):
        self = None
        data  = None
        self.data = data
        data.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    #add new elements in the list
    def append(self, data):
        new_node = node(data)
        curr = self.head

        while curr.next != None:
            curr = curr.next           
        curr.next = new_node

    #length of the list
    def length(self):
        curr = self.head
        total = 0
        while curr.next != None:
            total += 1
            curr= curr.next  
        return total

    def display(self):
        elms = []
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
            elms.append(curr_node.data)
        print(elms)

list = linkedlist()





