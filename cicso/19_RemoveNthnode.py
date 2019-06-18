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

def remove(head,n):
    dummy = ListNode(0)
    dummy.next = head
    ptr1 = dummy
    ptr2 = dummy
    #advance 1st prt by n nodes 0 to n, cuz 2 points to 
    # dummy(second)-->5--->10--->15(first)
    # dummy --->5---10----15(second)----20(second.next will be removed)----25---null(first)
    for i in range(n+1):
        ptr1 = ptr1.next
    while ptr1!=None:
        ptr1=ptr1.next
        ptr2=ptr2.next
    ptr2.next=ptr2.next.next
    return dummy.next
    #There is a possibility that head could be removed as it could be nth pointer from back
    

l5 = ListNode(25)
l4 = ListNode(20,l5)
l3 = ListNode(15,l4)
l2 = ListNode(10,l3)
l1 = ListNode(5,l2) 

print_ll(l1)
f = remove(l1,2)
print_ll(f)