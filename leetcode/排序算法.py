def bubbleSort(nums):
    # avg:n2 best:n worst:n2 space:1 inplace stable
    for i in range(1, len(nums)):
        for j in range(len(nums)-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

def selectionSort(nums):
    # avg:n2 best:n2 worst:n2 space:1 inplace unstable
    for i in range(len(nums)-1):
        minIndex = i
        for j in range(i+1,len(nums)):
            if nums[j] < nums[minIndex]:
                minIndex = j

        if i != minIndex:
            nums[i],nums[minIndex] = nums[minIndex],nums[i]

def insertionSort(nums,gap=1):
    # avg:n2 best:n worst:n2 space:1 inplace stable
    for i in range(gap,len(nums)):
        j = i-gap
        curr = nums[i]
        while j >= 0 and nums[j] > curr:
            nums[j+gap] = nums[j]
            j -= gap
        nums[j+gap] = curr

def shellSort(nums,gaps = [5,3,1]):
    for gap in gaps:
        insertionSort(nums, gap)

def heapSort(nums):
    import heapq
    size = len(nums)
    heap = nums[:]
    heapq.heapify(heap)
    return [heapq.heappop(heap) for _ in range(size)]

def mergeSort(nums):
    def merge(left,right):
        output = []
        while left and right:
            if left[0] <= right[0]:
                output.append(left.pop(0))
            else:
                output.append(right.pop(0))
        while left:
            output.append(left.pop(0))
        while right:
            output.append(right.pop(0))
        return output

    def helper(nums=nums):
        if len(nums) < 2:
            return nums
        mid = len(nums)//2
        return merge(helper(nums[:mid]),helper(nums[mid:]))

    return helper()


def quickSort(nums):

    def patition(left,right):
        pivot = left
        index = pivot + 1

        for i in range(left+1, right+1):
            if nums[i] < nums[pivot]:
                nums[i],nums[index] = nums[index],nums[i]
                index += 1
        nums[pivot], nums[index-1] = nums[index-1], nums[pivot]
        return index - 1

    def helper(left=0,right=len(nums)-1):
        if left < right:
            index = patition(left,right)
            helper(left,index-1)
            helper(index+1,right)

    helper()

def contingSort(nums):
    # 计数排序（整数空间）
    minNums = min(nums)
    maxNums = max(nums)
    size = maxNums-minNums+1

    bucket = [0] * size
    index = 0

    for n in nums:
        bucket[n] += 1

    for i in range(minNums, maxNums+1):
        while bucket[i]:
            nums[index] = i
            index += 1
            bucket[i] -= 1



if __name__ == '__main__':
    import random
    nums = [random.randint(-100,100) for _ in range(50)]
    cpNums = nums[:]
    cpNums.sort()
    # nums = [43,54,1,5,78,9,1000,3,13,75,77567]
    # bubbleSort(nums)
    # selectionSort(nums)
    # insertionSort(nums)
    # shellSort(nums)

    # output = heapSort(nums)
    # output = mergeSort(nums)
    # print(output == cpNums)
    quickSort(nums)
    # contingSort(nums)
    print(nums == cpNums)
