
def it(n=5):
    if n == 0:
        return 0

    return it(n-1) + 1

it()

def xx():
    global x
    x=3

nums = [-2,1,-3,4,-1,2,1,-5,4]



res = float('-inf')


for i in range(1, len(nums)):
    nums[i] = max(nums[i], nums[i] + nums[i - 1])
    res = max(res, nums[i])

print(res)
