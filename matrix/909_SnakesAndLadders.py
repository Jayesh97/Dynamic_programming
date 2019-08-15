import collections
board = [
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]]
def moves(board):
    n = len(board)
    def get(s):
        quot,rem = divmod(s-1,n)
        row = n-1-quot #6-1-(0)
        col = rem if row%2!=n%2 else n-1-rem #shuffles 
        return row,col
    dist = {1:0}
    queue = collections.deque([1])
    while queue:
        #print("queue",queue)
        s = queue.popleft()
        if s==n**2: return dist[s]
        #get possibilities of next step
        for s2 in range(s+1,min(s+6,n*n)+1):
            r,c = get(s2)
            if board[r][c]!=-1:
                s2 = board[r][c]
            if s2 not in dist:
                dist[s2]=dist[s]+1
                queue.append(s2)
    return 0
print(moves(board))
