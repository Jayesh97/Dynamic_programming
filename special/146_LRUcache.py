from collections import deque

class LRUcache():
    def __init__(self,capacity):
        self.capacity = capacity
        self.cache = {}
        self.queue = deque([])

    def get(self,key):
        value = self.cache.get(key,-1)
        if value != -1:
            self.queue.remove(key)
            self.queue.add(key) #Moving its position to the right most end
        return value

    def put(self,key,value):
        if self.cache.get(key,-1)!=-1:
            self.cache[key]=value
            self.queue.remove(key)
            self.queue.add(key)
        elif len(self.queue) == self.capacity:
            removed = self.queue.popleft()
            self.cache[removed]=-1
            self.cache[key]=value
            self.queue.add(key)
        else:
            self.queue.add(key)
            self.cache[key]=value
            
