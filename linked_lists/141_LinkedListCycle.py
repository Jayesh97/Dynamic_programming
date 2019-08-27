class ListNode():
    def __init__(self,value,next=None):
        self.value=value
        self.next=next

def cycle(root):
    if root==None or root.next==None:
        return False
    ptr1 = root
    ptr2 = root.next
    while ptr1!=ptr2:
        print(ptr2.value,ptr2.next)
        if ptr2==None or ptr2.next==None:
            return False
        ptr1 = ptr1.next
        ptr2 = ptr2.next.next
    return True

l1 = ListNode(2)
l2 = ListNode(1,l1)
l3 = ListNode(4,l2)
l4 = ListNode(3,l3)
l1.next = l4

print(cycle(l2))