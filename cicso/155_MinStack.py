class Stack:
    
    def __init__(self):
        self.q = []

    def push(self,value):
        cur_min = self.get_min()
        if value < cur_min:
            cur_min = value
        self.q.append((value,cur_min))

    def get_min(self):
        if self.q == []:
            return "Empty"
        else:
            return self.q[-1][1]

    def top(self):
        if self.top == None:
            return "Empty"
        else:
            return self.q[-1][0]

    def pop(self):
        self.q.pop()

    def all(self):
        print(self.q)

s = Stack()
s.push(4)
s.push(5)
s.push(3)
s.all()
print(s.get_min())
s.pop()
print(s.get_min())
s.all()
        
