
def backtrack(word,i,j,row,column):
    if board[i][j]!=word[backtrack.l]:
        return
    visited.add((i,j))
    #print(visited)
    backtrack.l = backtrack.l+1
    if backtrack.l == len(word):
        backtrack.found = True
        return
    for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
        i1,j1 = i+di,j+dj
        if 0<=i1<row and 0<=j1<column and (i1,j1) not in visited:
            backtrack(word,i1,j1,row,column)
            if backtrack.found==True:
                return
    visited.remove((i,j))
    backtrack.l = backtrack.l-1

board =[['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']]

word = "C"

board = [["c","c","f"],
         ["a","a","i"],
         ["c","d","e"]]
word = "fie"

board = [["C","A","A"],
        ["A","A","A"],
        ["B","C","D"]]

word = "AAB"

row ,column = len(board),len(board[0])
backtrack.found = False
visited = set()
backtrack.l = 0
for i in range(row):
    for j in range(column):
        backtrack(word,i,j,row,column)
        if backtrack.found == True:
            break
    if backtrack.found==True:
        break
if backtrack.found==True:
    print("True")
else:
    print("False")
