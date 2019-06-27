#O(m+n)
matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 20
def binary_search(row,target):
    l = 0
    r = len(row)
    while l<=r:
        mid=(l+r)/2
        if row[mid]==target:
            return True
        if row[mid]>target:
            r = mid-1
        if row[mid]<target:
            l = mid+1
    return False

def search(matrix,target):
    if not matrix or not matrix[0]: return False
    rows = len(matrix)
    columns = len(matrix[0])
    for row in matrix:
        if row[-1]<target:
            continue
        if row[0]>target:
            return False
        if binary_search(row,target):
            return True
    return False

row = [1,4,7,11,15]
row = [2,5,8,12,19]
print(search(matrix,target))
#print(binary_search(row,target))
