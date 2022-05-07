import random
import time

str_time = time.time()
# a = [....]
# b = [....]

size = 3

a = [random.randint(-5, 5) for _ in range(size)]
b = [random.randint(-5, 5) for _ in range(size)]

print(a)
print(b)
output = []
curr = []


def dfs(target, start_i=0, start_j=0, step=0):
    output.append((target, step, curr[:]))
    if target == 0:
        return None
    for i in range(start_i, size):
        for j in range(start_j, size):
            curr.append((start_i, start_j))
            dfs(target - 2 * (a[i] - b[j]), i + 1, j + 1, step + 1)
            curr.pop()


target = sum(a) - sum(b)
dfs(target)
print(output)
print(len(output))
output.sort(key=lambda x: abs(x[0]))
print(output)

minStep = size
minTarget = output[0][0]
for n in output:
    if abs(n[0]) == minTarget:
        minStep = min(minStep, n[1])

print(minTarget, minStep)

print('%.5f' % (time.time() - str_time))

# ---------------------
import random
import time

str_time = time.time()
# a = [....]
# b = [....]

size = 5
a = [random.randint(-10000, 10000) for _ in range(size)]
b = [random.randint(-10000, 10000) for _ in range(size)]

sum_a = sum(a)
sum_b = sum(b)

con = a + b

min_con = min(con)

for i in range(2 * size):
    con[i] -= min_con

# con = [1, 3, 2, 9, 0, 0]
# size = 3

sum_con = sum(con)
vol = sum(con) // 2
dp = [[[0, []] for _ in range(vol + 1)] for _ in range(size + 1)]

for i in range(2 * size):
    for n in range(min(i, size), 0, -1):
        for j in range(vol, con[i] - 1, -1):
            if dp[n][j][0] < dp[n - 1][j - con[i]][0] + con[i]:
                dp[n][j][0] = dp[n - 1][j - con[i]][0] + con[i]
                dp[n][j][1] = dp[n - 1][j - con[i]][1][:] + [con[i]]
            # dp[n][j] = max(dp[n][j], dp[n - 1][j - con[i]] + con[i])

# print(dp[-1])
# print(dp)

print('min_sub:', abs(2 * dp[-1][-1][0] - sum_con))
new_a = dp[-1][-1][1]
new_b = []

for i in con:
    if i not in new_a:
        new_b.append(i)

print('con:', con)
print('a:', new_a)
print('b:', new_b)


print('%.5f' % (time.time() - str_time))
