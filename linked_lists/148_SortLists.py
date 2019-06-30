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

def merge(h1,h2):
    '''
    print(h1.value,h2.value)
    print("start")
    print_ll(h1)
    print("start2")
    print_ll(h2)
    print("end")
    '''
    dummy = ListNode(0)
    tail = dummy
    while h1 and h2:
        if h1.value<h2.value:
            tail.next = h1
            h1 = h1.next
        else:
            tail.next = h2
            h2 = h2.next
        tail = tail.next
    tail.next = h1 or h2
    '''
    print("tail1")
    print_ll(tail)
    print("tail2")
    print_ll(dummy)
    print("end dummy")
    '''
    return dummy.next

def sortlist(head):
    if not head or not head.next:
        return head
    pre = None
    slow = head
    fast = head
    while fast and fast.next:
        pre = slow
        slow = slow.next
        fast = fast.next.next
    pre.next = None #to breakup the link between 2 halves
    print("s",head.value,slow.value)
    return merge(sortlist(head),sortlist(slow))


l7 = ListNode(7)
l6 = ListNode(6,l7)
l5 = ListNode(-1,l6)
l4 = ListNode(4,l5)
l3 = ListNode(3,l4)
l2 = ListNode(-3,l3)
l1 = ListNode(1,l2)

f = sortlist(l1)
#print_ll(f)