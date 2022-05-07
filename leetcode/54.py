

matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]


matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]

matrix = [[6,9,7]]
left = 0
top = 0
bottom = len(matrix)
right = len(matrix[0])
res = []
counter = 0

while left < right or top < bottom:
    for i in range(left, right-1):
        res.append(matrix[top][i])

    for i in range(top, bottom-1):
        res.append(matrix[i][right-1])

    for i in range(right-1, left, -1):
        res.append(matrix[bottom-1][i])

    for i in range(bottom-1, top, -1):
        res.append(matrix[i][left])

    left+=1
    top+=1
    right-=1
    bottom-=1

print(res)

nums = [2,3,4]

n = len(nums)
output = [[]]

for num in nums:
    output += [curr + [num] for curr in output]



matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

matrix = [[1,2,3],[4,5,6],[7,8,9]]
m, n = len(matrix), len(matrix[0])
i, j = 0, -1
speed = 1

output = []

while m and n:

    for _ in range(n):
        j += speed
        output.append(matrix[i][j])

    for _ in range(m - 1):
        i += speed
        output.append(matrix[i][j])

    m, n = m - 1, n - 1
    speed *= -1