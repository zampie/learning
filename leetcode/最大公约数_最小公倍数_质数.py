import math
from functools import reduce

def gcd(a,b):
    # 辗转相除法 Euclidean Algorithm
    if b > a:
        a,b=b,a
    mod = a % b
    if mod == 0:
        return b
    return gcd(b,mod)

def gcd2(a,b):
    # 更相减损术
    if b > a:
        a,b=b,a
    sub = a - b
    if sub == 0:
        return b
    return gcd(b,sub)

def lcm(a,b):
    # (a,b)x[a,b]=ab 最大公约数 * 最小公倍数 = 两数之积
    return a*b//gcd(a,b)

def is_prime_number(x):
    # 暴力判断质数
    if x<=1:
        return False

    if x==2 or x==3:
        return True

    for i in range(2,x//2+1):
        if x % i == 0:
            return False
    return True

def prime_numbers(limit = 1000):
    # 暴力生成质数
    output = []
    for n in range(2,limit+1):
        if is_prime_number(n):
            output.append(n)

    return output

def gen_prime_numbers(limit = 1000):
    for n in range(2,limit+1):
        if is_prime_number(n):
            yield n

def pfd(x):
    # 分解质因数 Prime factor decomposition
    output = []
    if is_prime_number(x):
        return [x]

    for p in gen_prime_numbers(math.ceil(math.sqrt(x))):
        while x % p == 0:
            output.append(p)
            x = x // p

    return output

def lcm2(a,b):
    # 分解质因数法
    # 如果有几个质因数相同，则比较两数中哪个数有该质因数的个数较多，乘较多的次数
    pa, pb = pfd(a),pfd(b)
    da, db = {},{}

    for p in pa:
        if p not in da:
            da[p] = 1
        else:
            da[p]+= 1

    for p in pb:
        if p not in db:
            db[p] = 1
        else:
            db[p]+= 1

    for p in db:
        if p in da:
            da[p] = max(da[p],db[p])
        else:
            da[p] = db[p]

    lis = []

    for p in da:
        lis += [p] * da[p]

    return reduce(lambda x,y: x*y, lis)

if __name__ == '__main__':

    gcd(1997,615)
    gcd2(1997,615)
    lcm(36,270)
    lcm2(36,270)

    is_prime_number(8)

    primes = gen_prime_numbers(100000)

    len(primes)
    it = gen_prime_numbers(int(1e3))
    pfd(9)