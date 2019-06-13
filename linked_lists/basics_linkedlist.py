#Initializing a linked list
class LinkedListNode():
    def __init__(self,value,nextnode=None):
        self.value = value
        self.nextnode = nextnode


class LinkedList():

    def __init__(self,head=None):
        self.head = head
    '''
    Insert at the end could be as such
        1. If linked list is empty, the node becomes the head
        2. Traverse until the end and insert there
    '''
    def insert(self,value):
        #create a node to be inserted
        node = LinkedListNode(value)
        #if no head, make the node as head
        if self.head is None:
            self.head = node
            return
        currentnode = self.head
        while True:
            #When you are at the last node, add a next node at null value
            if currentnode.nextnode is None:
                currentnode.nextnode = node
                break
            currentnode = currentnode.nextnode

    def print_ll(self):
        currentnode = self.head
        while currentnode is not None:
            print(currentnode.value)
            currentnode = currentnode.nextnode
        print("None")

    def delete_node(self,value_to_del):
        currentnode = self.head
        pre_node = None
        while currentnode is not None:
            if currentnode.value == value_to_del:
                #if u want to delete a head node, make next node as head
                if pre_node == None:
                    new_head = currentnode.nextnode
                    self.head = new_head
                    return self.head
                #if it occurs anywhere else for a link bn prev_node and next_node
                pre_node.nextnode = currentnode.nextnode
                return self.head
            pre_node = currentnode
            currentnode = currentnode.nextnode
        return self.head





ll = LinkedList()
print(ll.head,"hhjh")
ll.insert("5")
ll.insert("6")
ll.insert("7")
ll.print_ll()
ll.delete_node("6")
ll.print_ll()