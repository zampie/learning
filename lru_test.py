import functools
import time
import utils
import sys

sys.setrecursionlimit(10000)


@functools.lru_cache()
def get_now_str(a):
    return time.strftime("%X", time.localtime())


def fibf(n):
    if n == 1:
        return 1
    return fibf(n - 1) + n


@functools.lru_cache()
def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return fib(n - 1) + fib(n - 2)


def fib2(n=20, a=1, b=1):
    if n == 1:
        return b
    return fib2(n - 1, b, a + b)


@utils.decorator_timer()
def run():
    print(fib2(2900))


if __name__ == '__main__':
    # run()

    print(get_now_str(1))
    # 13:46:27
    time.sleep(2)
    print(get_now_str(2))
    # 13:46:29
    time.sleep(2)
    print(get_now_str(1))
    # 13:46:27

    print(get_now_str.cache_info())
    # CacheInfo(hits=1, misses=2, maxsize=128, currsize=2)

    get_now_str.cache_clear()
    # 清空缓存, 下次要正常运行程序
