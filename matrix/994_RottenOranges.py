from collections import deque
grid = [[2,1,1],[1,1,0],[0,1,1]]
def rotten(grid):
    def dfs(x,y,dist):
        for nx,ny in [(x,y-1),(x,y+1),(x+1,y),(x-1,y)]:
            if nx>=0 and nx<m and ny>=0 and ny<n and grid[nx][ny]==1:
                grid[nx][ny]=2
                queue.append((nx,ny,dist+1))

    m = len(grid)
    n = len(grid[0])
    queue = deque()
    dist = 0
    #Append all 2's in the queue
    for x in range(m):
        for y in range(n):
            if grid[x][y]==2:
                queue.append((x,y,0))
    while queue:
        x,y,dist=queue.popleft()
        dfs(x,y,dist)
    for x in range(m):
        for y in range(n):
            if grid[x][y]==1:
                return -1
    return dist

print(rotten(grid))