import numpy as np
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

board = np.array(board)

def isValidArray(a):
    lis = []
    for i in a:
        if i !='.' and i in lis:
            return False
        else:
            lis.append(i)
    return True

for i in range(9):
    if isValidArray(board[i]) == False:
        print(False)
    if isValidArray(board[:,i]) == False:
        print(False)
    m, n = i//3*3, i%3*3
    if isValidArray(board[m:m+3,n:n+3].flatten()) == False:
        print(False)

print(True)