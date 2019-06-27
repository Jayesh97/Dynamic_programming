from collections import defaultdict
n = 4
courses = [[2,0],[1,0],[3,1],[3,2],[1,3]]
#[1,0] is a node

graph = defaultdict(list)
for x,y in courses:
    graph[x].append(y)
visited=[0]*n
print(graph)

def dfs(node):
    visited[node]=-1
    for child in graph[node]:
        print(child)
        if visited[child]==1:
            continue
        if visited[child]==-1:
            return False
        if not dfs(child):
            return False
    visited[node]=1
    return True

def schedule(n,courses):
    for node in range(n):
        if visited[node]==0:
            if not dfs(node):
                return False
    return True

print(schedule(n,courses))