""""class Robot:
    def __init__(self,name,colour):
        self.name = name
        self.colour = colour

    def introduce_self(self):
        print("My name is " + self.name)
        print("My colour is " + self.colour)

r1 = Robot("tom","red")
r1.introduce_self()"""
class node:
    data = None
    next_node = None

    def __init__(self,data):
        self.data = data
    def __repr__(self):
        return "<Node data: %s>" % self.data

class Linkedlist:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
        self.head = None

    def append(self,data):
        new_node = node(data)
        new_node.next_node = self.head
        self.head  = new_node





e1 = Linkedlist(1)
e2 = Linkedlist(2)
e3 = Linkedlist(3)
e4 = Linkedlist(4)

e1.nextval = e2
e2.nextval = e3
e3.nextval = e4
Linkedlist.append()

thisvalue = e1

while thisvalue:
        print(thisvalue.dataval)
        thisvalue = thisvalue.nextval
