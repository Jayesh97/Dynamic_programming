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

def merge(l1,l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if l1.value<=l2.value:
        temp = l1
        temp.next=merge(l1.next,l2)
    else:
        temp = l2
        temp.next=merge(l1,l2.next)
    return temp

l3 = ListNode(15)
l2 = ListNode(10,l3)
l1 = ListNode(5,l2) 

l6 = ListNode(20)
l5 = ListNode(3,l6)
l4 = ListNode(2,l5)

f = merge(l1,l4)
print_ll(f)