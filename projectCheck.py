#判断是否为奇数
def IsOdd(n: int):
    if n % 2 == 0:
        return False
    else:
        return True

def FindResult(timeList: list):
    if len(timeList) == 0:
        return 0

    # 此处看似重复，其实长度为1与长度为2的意义不同
    if len(timeList) == 1:
        return timeList[0]
    if len(timeList) == 2:
        return timeList[0]

    if IsOdd(len(timeList)):
        return FindResult(timeList[: -1]) + timeList[-2]
    
    ResultList = []
    for i in range(2, len(timeList), 2):
        ResultList.append(timeList[i - 1] + max(FindResult(timeList[: i]), FindResult(timeList[i: ])))
    return min(ResultList)


timeList = [1,1,9,9,2,2]
timeList = [60, 81, 44, 20, 86, 94, 9, 30, 15, 44, 12, 87, 79, 31, 80, 72, 13, 80, 19, 7, 18, 23, 83, 96]

#将数组变换为：执行到这一步总共需要多少时间
# temp = []
# for n in range(len(timeList)):
#     temp.append(sum(timeList[: n + 1]))
# timeList = temp

# 优化
for n in range(1, len(timeList)):
    timeList[n] += timeList[n-1]

print(FindResult(timeList))





# My style

import sys

def FindResult(timeList):
    size = len(timeList)
    if size == 0:
        return 0
    # min unit, the recursive termination condition
    if size == 1 or size == 2:
        return timeList[0]

    # decide size is odd or not
    if size % 2 != 0:
        return FindResult(timeList[:-1]) + timeList[-2]

    ResultList = []
    for i in range(2, size, 2):
        ResultList.append(timeList[i - 1] + max(FindResult(timeList[:i]), FindResult(timeList[i:])))
    return min(ResultList)


lines = []
for line in sys.stdin:
    lines.append(line)

# preprocess, change the form of array
timeList = [int(i) for i in lines[1].split()]
for n in range(1, len(timeList)):
    timeList[n] += timeList[n - 1]

print(FindResult(timeList))