def solution(M, N):
    def xor_product(n):
        if n % 4 == 0:
            return n
        elif n % 4 == 1:
            return 1
        elif n % 4 == 2:
            return n + 1
        elif n % 4 == 3:
            return 0

    if M == 0:
        M = 1
    return xor_product(M - 1) ^ xor_product(N)


def solution2(M, N):
    res = M
    for i in range(M+1, N+1):
        res = res ^ i
    return res

solution(10,2000)
solution2(10,2000)