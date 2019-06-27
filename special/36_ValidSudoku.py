board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

def validation(board):
    column_validation = [[] for i in range(9)]
    cell_validation = [[] for i in range(9)]
    for row in range(len(board)):
        row_validation = []
        for column in range(len(board[row])):
            value = board[row][column]
            if value == '.':
                continue
            #row validation
            if value not in row_validation:
                row_validation.append(value)
            else:
                return False
            #column validation
            if value not in column_validation[column]:
                column_validation[column].append(value)
            else:
                return False
            #Cell validation
            current_cell = 3*int(row/3)+int(column/3)
            if value not in cell_validation[current_cell]:
                cell_validation[current_cell].append(value)
            else:
                print("3")
                return False
    return True
            


print(validation(board))