
def feb1(n):
    a = 0
    b = 1

    for i in range(n):
        a, b = b, a+b
        print(b)
    return b


def feb2(n, a=0, b=1):
    print(b)
    if n == 0:
        return b
    return feb2(n-1, b, a+b)

def feb3(n):
    dp = [0] * (n+2)

    dp[0] = 0
    dp[1] = 1

    for i in range(2, len(dp)):
        dp[i] = dp[i-2] + dp[i-1]

    print(dp)
    return dp[-1]



if __name__ == '__main__':
    n = 5
    # res = feb1(n)
    # res = feb2(n)
    res = feb3(n)
    print("res: ", res)