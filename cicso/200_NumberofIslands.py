grid = [[1, 1, 0, 0, 0], 
        [0, 1, 0, 0, 1], 
        [1, 0, 0, 1, 1], 
        [0, 0, 0, 0, 0], 
        [1, 0, 1, 0, 1]] 

grid = [["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]]

def islands(grid):
    if not grid:
        return 0
    row = len(grid)
    column = len(grid[0])
    summ = 0
    for i in range(row):
        for j in range(column):
            if grid[i][j]=="0":
                continue
            else:
                summ = summ+1
                #dfs
                stack = []
                stack.append([i,j])
                while len(stack)!=0:
                    [p,q]=stack.pop()
                    if p>=1 and grid[p-1][q]=="1":
                        stack.append([p-1,q])
                    if p<row-1 and grid[p+1][q]=="1":
                        stack.append([p+1,q])
                    if q>=1 and grid[p][q-1]=="1":
                        stack.append([p,q-1])
                    if q<column-1 and grid[p][q+1]=="1":
                        stack.append([p,q+1])
                    grid[p][q]="0"
    return summ

print(islands(grid))
