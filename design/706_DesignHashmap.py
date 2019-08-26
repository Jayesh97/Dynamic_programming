class ListNode():
    def __init__(self,key,value):
        self.pair=(key,value)
        self.next=None

class Hashmap():

    def __init__(self):
        self.n=1000
        self.buckets=[None]*self.n

    def put(self,key,value):
        index=key%self.n
        if self.buckets[index]==None:
            self.buckets[index]=ListNode(key,value)
        else:
            cur_node=self.buckets[index]
            #traversing nodes
            while True:
                if cur_node.pair[0]==key:
                    cur_node.pair=(key,value)
                    return
                if cur_node.next==None:
                    break
                cur_node=cur_node.next
            cur_node.next=ListNode(key,value)

    def get(self,key):
        index = key%self.n
        cur_node = self.buckets[index]
        while cur_node:
            if cur_node.pair[0]==key:
                return cur_node.pair[1]
            else:
                cur_node=cur_node.next
        return -1
    
    def remove(self,key):
        index = key%self.n
        cur_node=prev_node=self.buckets[index]
        if cur_node==None:
            return
        if cur_node.pair[0]==key:
            self.h[index]=cur_node.next
        else:
            cur_node = cur_node.next
            while cur_node!=None:
                if cur_node.pair[0]==key:
                    prev_node.next=cur_node.next
                    break
                else:
                    cur_node,prev_node=cur_node.next,prev_node.next
            


obj = Hashmap()
obj.put(5,"raleigh")
print(obj.get(3))
obj.put(5,"cary")
print(obj.get(5))