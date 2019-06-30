board =     [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
def gameoflife(board):
    neighbors = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
    rows = len(board)
    columns = len(board[0])
    for i in range(rows):
        for j in range(columns):
            live_neighbors = 0
            for k in neighbors:
                r = i+k[0]
                c = j+k[1]
                if (r>=0 and r<rows) and (c>=0 and c<columns) and abs(board[r][c])==1:
                    live_neighbors = live_neighbors+1
            if board[i][j]==1 and live_neighbors<2 or live_neighbors>3:
                board[i][j]=-1
            if board[i][j]==0 and live_neighbors>3:
                board[i][j]=2
    for i in range(rows):
        for j in range(columns):
            if board[i][j]>0:
                board[i][j]=1
            else:
                board[i][j]=0

gameoflife(board)
print(board)