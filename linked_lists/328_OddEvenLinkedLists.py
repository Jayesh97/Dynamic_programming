class LinkedListNode():
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

def print_ll(head):
    currentnode = head
    while currentnode is not None:
        print(currentnode.value)
        currentnode = currentnode.next

def odd_even(head):
    if head == None:
        return None
    odd = head
    ehead = head.next
    even = head.next
    while even!=None and even.next!=None:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = ehead
    return head


l7 = LinkedListNode(7)
l6 = LinkedListNode(6,l7)
l5 = LinkedListNode(5,l6)
l4 = LinkedListNode(4,l5)
l3 = LinkedListNode(3,l4)
l2 = LinkedListNode(2,l3)
l1 = LinkedListNode(1,l2)

print_ll(l1)
f = odd_even(l1)
print_ll(f)