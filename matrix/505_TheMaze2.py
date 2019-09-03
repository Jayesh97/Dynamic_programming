import heapq
from heapq import heappop,heappush
maze = [[0,0,1,0,0],
[0,0,0,0,0],
[0,0,0,1,0],
[1,1,0,1,1],
[0,0,0,0,0]]
start = (0,4)
destination = (4,4)

def mazepath(maze,start,destination):
    m,n=len(maze),len(maze[0])
    queue = [(0,start[0],start[1])]
    stopped = {(start[0],start[1]):0}
    while queue:
        dist,x,y = heapq.heappop(queue)
        if (x,y)==destination:
            return dist
        #ball sliding left goes all the way to left
        for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
            nx,ny,d=x,y,0
            while nx+dx>=0 and nx+dx<m and ny+dy>=0 and ny+dy<n and maze[nx+dx][ny+dy]!=1:
                nx = nx+dx
                ny = ny+dy
                d = d+1
            if (nx,ny) not in stopped or dist+d<stopped[(nx,ny)]:
                stopped[(nx,ny)]=dist+d
                heapq.heappush(queue,(dist+d,nx,ny))
    return -1

print(mazepath(maze,start,destination))
