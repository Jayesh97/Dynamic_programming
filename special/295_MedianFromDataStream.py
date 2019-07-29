from heapq import *
class medianstream:
    def __init__(self):
        self.small = []
        self.large = []
    def addnum(self,num):
        if len(self.small)==len(self.large):
            #we are returning the largest number from the "small" heap as -ve(smallest(-ve)) == largest
            heappush(self.large,-heappushpop(self.small,-num))
        else:
            heappush(self.small,-heappushpop(self.large,num))
        print(self.small,self.large)
    def findmedian(self):
        if len(self.small)==len(self.large):
            return float(self.large[0]-self.small[0])/2.0
        else:
            return float(self.large[0])
ob = medianstream()
ob.addnum(5)
ob.addnum(3)
print(ob.findmedian())
ob.addnum(2)
print(ob.findmedian())
ob.addnum(4)
print(ob.findmedian())