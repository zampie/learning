import time


# 效率最高
def fibonacci_loop(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    a, b = 1, 2
    for i in range(n - 2):
        a, b = b, a + b
    return b


# 效率极低，每次递归调用两次自身
def fibonacci_rec1(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return fibonacci_rec1(n - 1) + fibonacci_rec1(n - 2)


# 迭代次数有上限
def fibonacci_rec2(n, a=1, b=2):
    if n == 1:
        return a
    else:
        return fibonacci_rec2(n - 1, b, a + b)


def fibonacci_gen(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b
        # 执行完后断点
        # print('gen:',a,b,n)


if __name__ == '__main__':
    str_time = time.time()
    print(fibonacci_loop(10000))
    print('cost: %f' % (time.time() - str_time))

    str_time = time.time()
    print(fibonacci_rec1(35))
    print('cost: %f' % (time.time() - str_time))

    str_time = time.time()
    print(fibonacci_rec2(100))
    print('cost: %f' % (time.time() - str_time))

    str_time = time.time()
    for f in fibonacci_gen(30):
        print(f)
    print('cost: %f' % (time.time() - str_time))

    gen = fibonacci_gen(2)
    type(gen)
    gen.__next__()


def helper(n, a, b):
    if n == 0:
        return a

    return helper(n - 1, b, a + b)