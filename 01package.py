lines = [[4, 5], [1, 2], [2, 4], [3, 4], [4, 5]]

# 01背包
# 二维解法
size, vol = lines[0]
dp = [[0] * (vol+1) for i in range(size+1)]

for i in range(1, size+1):
    v, w = lines[i]
    w = 1
    for j in range(vol+1):
        dp[i][j] = dp[i-1][j]
        if j >= v:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - v] + w)

print(dp)
print(dp[-1][-1])

# 一维解法
size, vol = lines[0]
dp = [0] * (vol+1)

for i in range(1, size+1):
    v, w = lines[i]
    for j in range(vol, v - 1, -1):
        dp[j] = max(dp[j], dp[j - v] + w)

print(dp)
print(dp[-1])

# 完全背包
# 2
size, vol = lines[0]
dp = [[0] * (vol+1) for i in range(size+1)]

for i in range(1, size+1):
    v, w = lines[i]
    for j in range(vol+1):
        dp[i][j] = dp[i-1][j]
        if j >= v:
            dp[i][j] = max(dp[i][j], dp[i][j - v] + w)

print(dp)
print(dp[-1][-1])

# 1
size, vol = lines[0]
dp = [0] * (vol+1)

for i in range(1, size+1):
    v, w = lines[i]
    for j in range(v, vol+1):
        dp[j] = max(dp[j], dp[j - v] + w)

print(dp)
print(dp[-1])

