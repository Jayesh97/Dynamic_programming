graph = [
  [1,1,1],
  [0,1,0],
  [1,1,1]
]

def findceleb(graph):
    x = 0
    n = len(graph)
    for i in range(n):
        if graph[x][i]==1: #assuming x is celeb,he doesnt know anyone above him
            x=i
    #checking he doesn't know anyone less than his number
    for i in range(x):
        if graph[x][i]==1:
            return -1
    #checking all knows him
    for i in range(n):
        if graph[i][x]==0:
            return -1
    return x

print(findceleb(graph))

