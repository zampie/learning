'''
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
示例 1:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true
示例 2:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
输出: false

# 优先行的遍历
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        i,j=0,0

        while i<len(matrix) and j < len(matrix[0]):

            if matrix[i][j] == target:
                return True
            elif target > matrix[i][-1]:
                i += 1
            elif matrix[i][j] < target:
                j += 1
            else:
                return False

        return False

# 二维二分搜索
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        if matrix[0][0] > target or matrix[-1][-1] < target:
            return False

        top,bottom = 0,len(matrix)
        left,right = 0,len(matrix[0])-1



        while top <= bottom:
            i = (top+bottom) // 2
            if matrix[i][-1] == target or matrix[i][0] == target:
                return True
            if matrix[i][-1] > target and matrix[i][0] < target:
                break
            if matrix[i][-1] < target:
                top = i + 1
            if matrix[i][0] > target:
                bottom = i - 1

        while left <=right:
            j = (left+right) // 2
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                left = j + 1
            else:
                right = j - 1



        return False





# 化为一维二分搜索
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        m,n = len(matrix[0]), len(matrix)
        left, right = 0, m*n-1

        while left <= right:
            mid = (left+right) // 2
            i,j = mid//m,mid%m
            curr = matrix[i][j]

            if target == curr:
                return True
            elif target > curr:
                left = mid+1
            else:
                right = mid-1


        return False

'''

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 10

top, bottom = 0, len(matrix) - 1
left, right = 0, len(matrix[0]) - 1

if matrix[0][0] > target or matrix[-1][-1] < target:
    print(False)

while top < bottom:
    i = (top + bottom) // 2
    if matrix[i][-1] == target or matrix[i][0] == target:
        print(True)
    if matrix[i][-1] < target:
        top = i + 1
    if matrix[i][0] > target:
        bottom = i - 1

while left <= right:
    j = (left + right) // 2
    if matrix[i][j] == target:
        print(True)
    elif matrix[i][j] < target:
        left = j + 1
    else:
        right = j - 1

print(False)