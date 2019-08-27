class ListNode():
    def __init__(self,value,next=None):
        self.value=value
        self.next=next

def cycle(head1,head2):
    if head1==None or head2==None:
        return None
    ptr1 = head1
    ptr2 = head2
    while ptr1!=ptr2:
        if ptr1==None:
            ptr1=head2
        else:
            ptr1=ptr1.next
        if ptr2==None:
            ptr2=head1
        else:
            ptr2=ptr2.next
    return ptr1.value

l1 = ListNode(2)
l2 = ListNode(1,l1)
l3 = ListNode(4,l2)
l4 = ListNode(3,l3)
l5 = ListNode(7,l2)

print(cycle(l4,l5))