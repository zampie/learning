n=5
triAngle = []
curList = [1]

for i in range(n):
    if i == 0:
        curList = [1]
    else:
        curList = [1] * (i + 1)
        for j in range(1,i):
            curList[j] = triAngle[i - 1][j - 1] + triAngle[i - 1][j]

    triAngle.append(curList)

print(triAngle)