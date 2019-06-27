class NestedIterator(object):

    def __init__(self, nestedList):
        self.stack = nestedList

        
    def next(self):
        if type(self.stack[0])==list:
            self.hasNext()
        return self.stack.pop(0)

    def hasNext(self):
        while self.stack:
            top = self.stack[0]
            if type(top)==int:
                return True
            self.stack = top+self.stack[1:]
        return False



    def print_ns(self):
        print(self.stack)

ns = [[1,1],2,[1,1]]
ns = [1,[4,[6]]]
#ns = [[1,[1]],2,[1,1]]
ns1 = NestedIterator(ns)
ns1.print_ns()
l = []
while ns1.hasNext():
    l.append(ns1.next())
print(l)
