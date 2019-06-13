def kthsmallest(matrix,k):
    def smallerthan(x):
        i,j = n-1,0
        count = 0
        while i>=0 and j<n:
            if matrix[i][j]>x:
                i = i-1
            else:
                j = j+1
                count = count + i + 1
        return count
    n = len(matrix)
    lo = matrix[0][0]
    high = matrix[n-1][n-1]
    while lo<high:
        mid = (lo+high)/2
        print(lo,high,smallerthan(mid))
        if smallerthan(mid)<k:
            lo = mid+1
        else:
            high = mid
    return lo

matrix = [
   [ 1,  5,  13],
   [10, 11, 13],
   [11, 11, 15]]
k = 8
print(kthsmallest(matrix,k))


