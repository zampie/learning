boxes = [[0, 0, 100, 100], [10, 10, 120, 120], [130, 130, 150, 150]]

# 阈值
th = 0.5

# box数量
size = len(boxes)

i = 0
j = 1
while i < size - 1:
    while j < size:
        xi0, yi0, xi1, yi1 = boxes[i]
        xj0, yj0, xj1, yj1 = boxes[j]

        if xi1 > xj0 and yi1 > yj0:
            # 相交面积
            area_cross = (xi1 - xj0) * (yi1 - yj0)
        else:
            area_cross = 0
            continue

        area_i = (xi1 - xi0) * (yi1 - yi0)
        area_j = (xj1 - xj0) * (yj1 - yj0)
        # 交并比
        iou = area_cross / (area_i + area_j - area_cross)

        if iou > th:
            xi1, yi1 = xj1, yj1
            boxes[i] = [xi0, yi0, xi1, yi1]
            boxes.pop(j)
            size -= 1
        j += 1

    i += 1
    j = i+1

# 时间复杂度 n^2
# 空间复杂度 n^2
# n = box数量