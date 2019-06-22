matrix = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]

def setzeros(matrix):
        row = len(matrix)
        column = len(matrix[0])
        rows_list = set()
        columns_list = set()

        #marking
        for i in range(row):
            for j in range(column):
                if matrix[i][j]==0:
                    rows_list.add(i)
                    columns_list.add(j)
        for i in range(row):
            for j in range(column):
                if i in rows_list or j in columns_list:
                    matrix[i][j]=0

        return matrix

def setzeros2(matrix):
    row = len(matrix)
    column = len(matrix[0])
    is_column=False
    for i in range(row):
        if matrix[i][0]==0:
            is_column=True
        for j in range(1,column):
            if matrix[i][j]==0:
                matrix[0][j]=0
                matrix[i][0]=0
    for i in range(1,row):
        for j in range(1,column):
            if matrix[i][0]==0 or matrix[0][j]==0:
                matrix[i][j]=0
    if matrix[0][0]==0:
        for j in range(column):
            matrix[0][j]=0
    if is_column:
        for i in range(row):
            matrix[i][0]=0
    
print(setzeros(matrix))