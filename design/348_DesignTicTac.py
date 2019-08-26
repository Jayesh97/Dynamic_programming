n = 3
class TictacToe(object):
    def __init__(self,n):
        self.d = {}
        self.n = n

    def move(self,row,col,player):
        d = self.d
        for i,j in enumerate((row,col,row+col,row-col)):
            d[i,j,player]=d.get((i,j,player),0)+1
            #print(self.d)
            if d[i,j,player]==n:
                return player
        return 0

obj = TictacToe(3)
f = obj.move(0,0,1)
f = obj.move(0,2,2)
f = obj.move(1,0,1)
f = obj.move(2,2,2)
f = obj.move(2,0,1)
print(f)
