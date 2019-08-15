import collections
forest = [
 [1,2,3],
 [0,0,4],
 [7,6,5]
]

def cutting(forest):
    row = len(forest)
    column = len(forest[0])
    trees_to_cut = []
    for i in range(row):
        for j in range(column):
            if forest[i][j]>1:
                trees_to_cut.append((forest[i][j],i,j))
    trees_to_cut = sorted(trees_to_cut)
    #print(trees_to_cut)
    count = 0
    cx,cy=0,0 #(x,y) co-ordinates to be taken
    for height,x,y in trees_to_cut:
        step = bfs(forest,cx,cy,x,y)
        if step==-1:
            return -1
        else:
            count = count+step
            forest[x][y]=1
            cx,cy=x,y
    return count

def bfs(forest,cx,cy,tx,ty):
    row = len(forest)
    column = len(forest[0])
    visited = [[False for j in range(column)] for i in range(row)]
    queue = collections.deque()
    step = -1
    queue.append((cx,cy))
    while len(queue)>0:
        step = step + 1
        for i in range(len(queue)):
            x,y = queue.popleft()
            visited[x][y]= True
            if x == tx and y == ty:
                return step
            for new_x, new_y in [(x+1,y),(x-1,y),(x,y-1),(x,y+1)]:
                if new_x<0 or new_x>=row or new_y<0 or new_y>=column or forest[new_x][new_y]==0 or visited[new_x][new_y]==True:
                    continue
                queue.append((new_x,new_y))
    return -1 #To show step is unreachable

print(cutting(forest))