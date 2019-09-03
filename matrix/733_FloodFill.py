from collections import deque
image = [[0,0,0],[0,1,1]]
sr = 1
sc = 1
newColor = 1

def floodfill(image,sr,sc,newColor):
    def dfs(x,y):
        for nx,ny in [(x+1,y),(x-1,y),(x,y-1),(x,y+1)]:
            if nx>=0 and nx<m and ny>=0 and ny<n and image[nx][ny]==start_color and visited[nx][ny]==False:
                image[nx][ny]=newColor
                queue.append((nx,ny))

    queue=deque()
    m=len(image)
    n=len(image[0])
    start_color = image[sr][sc]
    if start_color==newColor:
        return image
    visited=[[False for i in range(n)] for j in range(m)]
    image[sr][sc]=newColor
    queue.append((sr,sc))
    while queue:
        #print(queue)
        x,y = queue.popleft()
        visited[x][y]=True
        if image[x][y]==newColor:
            dfs(x,y)
    #print(image)
    return image

floodfill(image,sr,sc,newColor)
print(image)
        