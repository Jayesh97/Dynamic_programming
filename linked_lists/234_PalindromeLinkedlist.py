class ListNode(object):
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

class Palin(object):
    def ispalin(self,head):
        l = []
        while head==None:
            return True
        while head.next!=None:
            l.append(head.val)
            head = head.next
        l.append(head.val)
        return l==l[::-1]

l1 = ListNode(5)
l2 = ListNode(3,l1)
l3 = ListNode(1,l2)
l4 = ListNode(3,l3)
l5 = ListNode(5,l4)

obj = Palin()
print(obj.ispalin(l5))


