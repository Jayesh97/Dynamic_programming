class LinkedListNode():

    def __init__(self,value,nextnode=None):
        self.value = value
        self.nextnode = nextnode
    

def merge(l1,l2):
    if l1 == None:
        return l2
    if l2 == None:
        return l1
    if l1.value < l2.value:
        l1.nextnode = merge(l1.nextnode,l2)
        return l1
    else:
        l2.nextnode = merge(l1,l2.nextnode)
        return l2

def print_ll(node):
    while True:
        if node == None:
            return
        print(node.value)
        node = node.nextnode
        


n3 = LinkedListNode(5,None)
n2 = LinkedListNode(3,n3)
n1 = LinkedListNode(1,n2)
l1 = n1

m3 = LinkedListNode(4,None)
m2 = LinkedListNode(2,m3)
m1 = LinkedListNode(0,m2)
l2 = m1

merged = merge(l1,l2)
print_ll(merged)