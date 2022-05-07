'''

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            if target in matrix[i]:
                return True

        return False



'''


matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

target = 20

matrix = [[-5]]
target = [-5]

n = len(matrix)
m = len(matrix[0])
i = 0
j = m - 1

while i < n and j >= 0:
  if matrix[i][j] == target:
    print(True)
  elif matrix[i][j] < target:
    i += 1
  else:
    j -= 1

print(False)