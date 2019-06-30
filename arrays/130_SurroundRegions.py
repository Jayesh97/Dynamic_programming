board = [["X","X","X","X"],
["X","O","O","X"],
["X","X","O","X"],
["X","O","X","X"]]

def surround(board):
    if not board:
        return 
    m = len(board)
    n = len(board[0])
    def expand(i,j):
        neighbors = [(1,0),(0,1),(-1,0),(0,-1)]
        ans = []
        for (x,y) in neighbors:
            r = i+x
            c = j+y
            if (r>=0 and r<m) and (c>=0 and c<n) and board[r][c]=="O":
                ans.append([r,c])
        return ans
    #recursing over a certain point to convert all "O" to "S"
    def dfs(i,j):
        board[i][j]="S"
        for neighbor in expand(i,j):
            x,y = neighbor
            dfs(x,y)
    #expand around borders to find the unrestricted "O"s
    for i in range(m):
        if board[i][0]=="O":
            dfs(i,0)
        if board[i][n-1]=="O":
            dfs(i,n-1)
    for i in range(n):
        if board[0][i]=="O":
            dfs(0,i)
        if board[m-1][i]=="O":
            dfs(m-1,i)
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            if board[i][j] == 'S':
                board[i][j] = 'O'
    print(board)
surround(board)