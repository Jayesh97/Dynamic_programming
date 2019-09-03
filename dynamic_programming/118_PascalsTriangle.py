total_rows = 5
def pascals_triagle(total_rows):
    trianle=[]
    for row_no in range(total_rows):
        #running another for loop is also valid
        row = [None for i in range(row_no+1)]
        row[0],row[-1]=1,1
        for j in range(1,row_no):
            row[j]=trianle[row_no-1][j-1]+trianle[row_no-1][j]
        trianle.append(row)
    return trianle

print(pascals_triagle(total_rows))
