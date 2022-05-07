def couldAdd(row, col):
    for queen in queens:
        if row == queen[0] or col == queen[1]:
            return False
    if row - col not in mainDiag:
        mainDiag[row - col] = True
    if row + col not in antiDiag:
        antiDiag[row + col] = True
    return mainDiag[row - col] and antiDiag[row + col]

def addQueen(row, col):
    queens.add((row, col))
    mainDiag[row - col] = False
    antiDiag[row + col] = False

def removeQueen(row, col):
    queens.remove((row, col))
    mainDiag[row - col] = True
    antiDiag[row + col] = True

# def addSolution(queens):
#     matrix = [['.'] * n for _ in range(n)]
#     for row,col in queens:
#         matrix[row][col] = 'Q'
#     output.append(matrix)

def addSolution(queens):
    solution = []
    for row, col in sorted(queens):
        solution.append(col * '.' + 'Q' + (n - col -1) * '.')
    output.append(solution)

def dfs(row=0, col=0):
    if row == n:
        addSolution(queens)
        return

    for i in range(n):
        if couldAdd(row, i):
            addQueen(row, i)
            dfs(row+1, 0)
            removeQueen(row, i)



n = 8
queens = set()
mainDiag = {}
antiDiag = {}
output = []

dfs()

print(len(output))
print(output)