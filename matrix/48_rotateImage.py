def transpose(matrix,m,n):
    for i in range(n):
        for j in range(i,m):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    return matrix
def reverse(matrix,m,n):
    for i in range(n):
        for j in range(m/2): #only half to swap
            if j<m/2:
                matrix[i][j],matrix[i][m-j-1]=matrix[i][m-j-1],matrix[i][j]
    return matrix
matrix = [[1, 2, 3], 
        [5, 6, 7], 
        [9, 10, 11], 
        [13, 14, 15]]
n = len(matrix) #rows
m = len(matrix[0]) #columns
print(transpose(matrix,m,n))
print(reverse(matrix,m,n))