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

def reverse(l1):
    prev = None
    curr = l1
    while curr!=None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    l1 = prev
    return l1

def reorder(l1):
    slow = l1
    fast = l1.next
    while fast!=None and fast.next!=None:
        slow = slow.next
        fast = fast.next.next
    node1 = l1
    node2 = slow.next
    slow.next = None #breaks the link bn l1 and l2
    node2 = reverse(node2)
    dummy = ListNode(0)
    curr = dummy
    while node1!=None or node2!=None:
        if node1!=None:
            curr.next=node1
            curr = curr.next
            node1 = node1.next
        if node2!=None:
            curr.next=node2
            curr=curr.next
            node2=node2.next
    return dummy.next



l5 = ListNode(25)
l4 = ListNode(20,l5)
l3 = ListNode(15,l4)
l2 = ListNode(10,l3)
l1 = ListNode(5,l2)

#print_ll(l1)
f = reorder(l1)
print_ll(f)
print_ll(l1)

