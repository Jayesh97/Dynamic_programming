matrix = [ [1, 2, 3, 4, 5, 6], 
      [7, 8, 9, 10, 11, 12], 
      [13, 14, 15, 16, 17, 18] ] 
l = []
r1 = 0
r2 = len(matrix)
c1 = 0
c2 = len(matrix[0])
while r1<r2 and c1<c2:
    #1st row
    for i in range(c1,c2):
        l.append(matrix[r1][i])
    r1 = r1+1
    #last column
    for i in range(r1,r2):
        l.append(matrix[i][c2-1])
    c2 = c2-1
    if r1<r2:
        #last row
        for i in range(c2-1,c1-1,-1):
            l.append(matrix[r2-1][i])
        r2 = r2-1
    if c1<c2:
        for i in range(r2-1,r1-1,-1):
            l.append(matrix[i][c1])
        c1=c1+1
print(l)