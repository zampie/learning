
m = 7
n = 3

mat = [[1 ] *m ] *n

for i in range(1, n):
    for j in range(1, m):
        mat[i][j] = mat[i - 1][j] + mat[i][j - 1]