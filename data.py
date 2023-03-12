#MAKEING A LINKLIST

class node:
    data = None
    next_node = None

    def __init__(self,data):
        self.data = data
    def __repr__(self):
        return "<Node data: %s>" % self.data
    
class Linked_list:
    def __init__(self):
        self.head = None

    def empty(self):
        return self.head == None

#size of the list
    def size(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node
        return count

#ADDING NEW ELEMENTS
    def add(self,data):
        new_node = node(data)
        new_node.next_node = self.head
        self.head = new_node
        

    def __repr__(self):
        node = []
        current = self.head

        while current:
            if current is self.head:
                node.append("[head %s]" % current.data)
            elif current.next_node is None:
                node.append("[tail: %s]" % current.data)
            else:
                node.append("[%s]" % current.data)

            current = current.next_node
        return '-> '.join(node)

l = Linked_list()
l.add(1)
l.add(9)
l.add(3)
print(l)