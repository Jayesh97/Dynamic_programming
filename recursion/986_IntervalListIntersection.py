A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]
def intervalintersection(A,B):
    res = []
    i=j=0
    while i<len(A) and j<len(B):
        low = max(A[i][0],B[j][0])
        high = min(A[i][1],B[j][1])
        if low<=high:
            res.append([low,high])
        if A[i][1]<B[j][1]:
            i=i+1
        else:
            j=j+1
    return res
print(intervalintersection(A,B))
