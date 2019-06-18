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

l5 = ListNode(25)
l4 = ListNode(20,l5)
l3 = ListNode(15,l4)
l2 = ListNode(10,l3)
l1 = ListNode(5,l2) 

def reverse(head,m,n):
    if not head:
        return None
    curr = head
    prev = None
    while m>1:
        prev = curr
        curr = curr.next
        m = m-1
        n = n-1
    tail = curr
    con = prev
    while n:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        n = n-1
    if con:
        con.next=prev
    else:
        head=prev
    tail.next = curr
    return head

f = reverse(l1,2,4)
print_ll(f)


