matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
def teomatrix(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if r>0 and c>0 and matrix[r-1][c-1]!=matrix[r][c]:
                return False
    return True

print(teomatrix(matrix))