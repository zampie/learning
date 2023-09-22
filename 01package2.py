from itertools import count


cost = [1, 3, 4]
value = [15, 20, 30]
max_cost = 4

size = len(cost)

dp = [[0] * (max_cost + 1) for _ in range(size + 1)]


for i in range(1, size + 1):
    for j in range(1, max_cost + 1):
        if cost[i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-cost[i-1]] + value[i-1], dp[i-1][j])
    
print(dp)


dp = [0] * (max_cost + 1)


for i in range(1, size + 1):
    for j in range(max_cost, cost[i-1] - 1, -1):
        dp[j] = max(dp[j-cost[i-1]] + value[i-1], dp[j])
    
print(dp)




dp = [[0] * (max_cost + 1) for _ in range(size + 1)]


for i in range(1, size + 1):
    for j in range(1, max_cost + 1):
        if cost[i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i][j-cost[i-1]] + value[i-1], dp[i-1][j])
    
print(dp)



dp = [0] * (max_cost + 1)


for i in range(1, size + 1):
    for j in range(cost[i-1], max_cost + 1):
        dp[j] = max(dp[j-cost[i-1]] + value[i-1], dp[j])
    
print(dp)

