import sys

lines = []
for line in sys.stdin.readlines():
    # print(line)
    lines.append(line)


print(lines)

M, K, N = [int(i) for i in lines[0].split()]
A = []
B = []
C = [[0] * N for _ in range(M)]

for j in range(1, M + 1):
    A.append([int(i) for i in lines[j].split()])

for j in range(M + 1, M + K + 1):
    B.append([int(i) for i in lines[j].split()])

for m in range(M):
    for n in range(N):
        for k in range(K):
            C[m][n] = A[m][k] * B[k][n]

print(C)
