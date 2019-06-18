class ListNode():
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

def print_ll(l1):
    print("start")
    while l1.next!=None:
        print(l1.value)
        l1= l1.next
    print(l1.value)
    print("End")

def reverse(head):
    if head==None or head.next==None:
        return head
    temp=reverse(head.next)
    head.next.next=head
    head.next=None
    return temp


l3 = ListNode(15)
l2 = ListNode(10,l3)
l1 = ListNode(5,l2) 

f = reverse(l1)
print_ll(f)