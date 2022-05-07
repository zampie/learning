
nums = [2,3,3,5,3]

for i in range(len(nums)):
    if nums[i] == 3:
        nums.pop(i)
    print(nums)

map(lambda x:x**2, nums)


s = "abcdefg"
k = 2
for i in range(0, len(s), 2 * k):
    print(i)

    left = i - 1 if i - 1 != -1 else None
    right = i + k - 1
    s = s[:i] + s[right:left:-1] + s[i+k:]
print(s)


mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]

for i in range(len(mat)):
    mat[i].append(i)

for e in enumerate(['a', 'b', 'c']):
    print(e)

enu = enumerate(mat)

res = [i[0] for i in sorted(enu, key=lambda x:sum(x[1]))[:k]]
