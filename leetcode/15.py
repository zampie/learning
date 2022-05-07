nums = [-1, 0, 1, 2, -1, -4]

dic = {}
res = []
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        c = -nums[i] - nums[j]
        if c in dic and dic[c] != j:
            res.append([i, j, dic[c]])
    dic[nums[i]] = i

print(res)