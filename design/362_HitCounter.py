from collections import deque

class Hitcounter(object):

    def __init__(self):
        self.hits=0
        self.time_hits=deque()

    def hit(self,timestamp):
        #if queue is empty === not self.time_hits
        if self.time_hits==deque() or self.time_hits[-1][0]!=timestamp:
            self.time_hits.append([timestamp,1])
        else:
            self.time_hits[-1][1]+=1
        self.hits+=1

    def gethits(self,timestamp):
        while self.time_hits and self.time_hits[0][0]<=timestamp-300:
            self.hits=self.hits-self.time_hits.popleft()[1]
        return self.hits

obj=Hitcounter()
obj.hit(1)
obj.hit(2)
f = obj.gethits(20)
print(f)