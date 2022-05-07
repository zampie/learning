def binary_search_loop(arr, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        print('left:arr[%d]=%d, mid:arr[%d]=%d, right:arr[%d]=%d' % (left, arr[left], mid, arr[mid], right, arr[right]))
        if arr[mid] == target:
            return (mid)
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1


def binary_search_recursive(arr, target, left, right):
    mid = (left + right) // 2
    print('left:arr[%d]=%d, mid:arr[%d]=%d, right:arr[%d]=%d' % (left, arr[left], mid, arr[mid], right, arr[right]))
    if left <= right:
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search_recursive(arr, target, left, mid - 1)
        else:
            return binary_search_recursive(arr, target, mid + 1, right)


if __name__ == '__main__':
    arr = [1, 3, 4, 5, 6, 76, 129, 300, 400, 1000]
    target = 450
    left, right = 0, len(arr) - 1

    print(binary_search_loop(arr, target, left, right))
    print(binary_search_recursive(arr, target, left, right))

nums = [5, 7, 7, 8, 8, 10]
target = 8

left, right = 0, len(nums) - 1

while left <= right:
    mid = (left + right) // 2
    if nums[mid] >= target:
        right = mid - 1
    else:
        left = mid + 1

start = left

left, right = 0, len(nums) - 1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] <= target:
        left = mid + 1
    else:
        right = mid - 1
end = right

import random

nums = [random.randint(-100, 100) for _ in range(20)]
nums.sort()
size = len(nums)
target = nums[random.randint(0, len(nums) - 1)]

left, right = 0, size - 1

while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        break
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

if nums[mid] == target:
    print(mid, target)