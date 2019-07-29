class ListNode():
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

def print_ll(node):
    while True:
        if node == None:
            return
        print(node.value)
        node = node.next

def mergek(lists):
    n = len(lists)
    step = 1
    while step<n:
        for i in range(0,n-step,step*2):
            lists[i]=merge2lists(lists[i],lists[i+step])
        step = step*2
    return lists[0] if n>1 else None

def merge2lists(l1,l2):
    dummy = ListNode(0)
    tail = dummy
    while l1 and l2:
        if l1.value<=l2.value:
            tail.next=l1
            l1=l1.next
        else:
            tail.next=l2
            l2=l2.next
        tail=tail.next
    if l1:
        tail.next = l1
    else:
        tail.next = l2
    return dummy.next


l4 = ListNode(9)
l3 = ListNode(6,l4)
l2 = ListNode(5,l3)
l1 = ListNode(3,l2)

ll4 = ListNode(8)
ll3 = ListNode(7,ll4)
ll2 = ListNode(4,ll3)
ll1 = ListNode(2,ll2)

al4 = ListNode(14)
al3 = ListNode(12,al4)
al2 = ListNode(3,al3)
al1 = ListNode(1,al2)


lists = []

f = mergek(lists)

print_ll(f)