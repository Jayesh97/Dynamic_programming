class ListNode():
    def __init__(self,value,next=None,random=None):
        self.value = value
        self.next = next
        self.random = random

def print_ll(l1):
    print("start")
    while l1.next!=None:
        print(l1.value,"----",l1.random)
        l1= l1.next
    print(l1.value,"----",l1.random)
    print("End")

def copy_random(l1):
    curr1 = l1
    curr2 = None
    d = {}
    while curr1!=None:
        curr2 = ListNode(curr1.value)
        d[curr1]=curr2
        curr1 = curr1.next
    curr1 = l1
    while curr1!=None:
        curr2 = d[curr1]
        curr2.next = curr1.next
        curr2.random = curr1.random
        curr1 = curr1.next
    return d[l1]

l5 = ListNode(5)
l4 = ListNode(4,l5)
l3 = ListNode(3,l4)
l2 = ListNode(2,l3)
l1 = ListNode(1,l2)

l1.random = l3
l2.random = l4
l3.random = l5
l4.random = l1
l5.random = l2

print_ll(l1)
f = copy_random(l1)
print_ll(f)