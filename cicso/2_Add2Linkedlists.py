class ListNode():
    def __init__(self,value,next=None):
        self.value = value
        self.next = next



l3 = ListNode(3)
l2 = ListNode(4,l3)
l1 = ListNode(2,l2) 

l6 = ListNode(4)
l5 = ListNode(6,l6)
l4 = ListNode(5,l5)

def print_ll(l1):
    print("start")
    while l1.next!=None:
        print(l1.value)
        l1= l1.next
    print(l1.value)
    print("End")

def add_ll(l1,l2):
    dummy = ListNode(0)
    carry = 0
    curr = dummy
    while(l1!=None or l2!=None):
        print("hi")
        x = 0 if l1==None else l1.value
        y = 0 if l2==None else l2.value
        summ = x+y+carry
        carry = summ/10
        curr.next = ListNode(summ%10)
        curr = curr.next
        if l1!=None : l1 = l1.next
        if l2!=None : l2 = l2.next
    if carry>0:
        curr.next = ListNode(carry)
    print(dummy)
    print(curr)
    return dummy.next

#add_ll(l1,l4)
f = add_ll(l1,l4)
print_ll(l1)
print_ll(l4)
print_ll(f)
        