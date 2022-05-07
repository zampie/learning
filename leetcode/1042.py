# paths = [[1, 2], [2, 3], [3, 1]]
paths = []
n = 10
G = {}
for x, y in paths:
    if x not in G:
        G[x] = [y]
    else:
        G[x].append(y)
    if y not in G:
        G[y] = [x]
    else:
        G[y].append(x)


ans = [0] * n
total_colors = {1, 2, 3, 4}
for x in range(1, n + 1):
    if x in G:
        band_colors = {ans[i - 1] for i in G[x]}
    else:
        band_colors = set()
    colors = total_colors - band_colors
    ans[x - 1] = colors.pop()

print(ans)
