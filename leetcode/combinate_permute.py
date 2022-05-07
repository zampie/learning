from itertools import permutations

res = []

def combination(nums, curr, start):
    if not nums:
        return
    res.append(curr[:])

    for i in range(start, len(nums)):
        curr.append(nums[i])
        combination(nums, curr, i+1)
        curr.pop()


if __name__ == '__main__':
    nums = list(range(5))
    combination(nums, [], 0)
    print(res)


