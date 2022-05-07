import os
import time
from functools import wraps
from collections import Iterable, deque

import numpy as np
import cv2


# 普通函数装饰器, 最外层为了输入参数, 如果没有参数可以省略
def decorator_timer(timer_unit="ms"):
    # 第二层, 主体部分
    def timer(fun):
        # print(fun.__name__ + " timer: init")
        # 此处是为了让外部访问fun.__name__的值不发生变化, 不加变为wraper
        @wraps(fun)
        def wrapper(*args, **kwargs):  # 接受任意参数

            print("args: ", args)
            time_str = time.time()

            print(fun.__name__, ": start")
            res = fun(*args, **kwargs)

            time_cost = time.time() - time_str

            unit = timer_unit
            if unit == "ms":
                time_cost = time_cost * 1000
            elif unit == "min":
                time_cost = time_cost / 60
            elif unit == "h":
                time_cost = time_cost / 3600
            else:
                unit = "s"
                # 不能这么写! timer_unit是闭包变量, 新建局部变量timer_unit会覆盖闭包变量, 导致上面找不到timer_unit
                # 如果要 改变timer_unit的话, 需要用 nonlocal timer_unit 声明闭包变量
                # timer_unit = "s"

            print(fun.__name__ + " cost: %.3f " % time_cost + unit)
            return res

        return wrapper

    return timer


# 类装饰器, 实现简单, 不接受额外参数
class ClassDecoratorTimer:
    def __init__(self, fun):
        self.fun = fun

    def __call__(self, *args, **kwargs):
        print("args: ", args)
        time_str = time.time()

        print(self.fun.__name__, ": start")
        res = self.fun(*args, **kwargs)

        time_cost = time.time() - time_str

        print(self.fun.__name__ + " cost: %.3f " % time_cost + 's')
        return res


# 对象装饰器, 跟函数装饰器基本相同, 额外参数在初始化时复制, wrapper要外包@wraps防止函数名变化
class ObjectDecoratorTimer:
    def __init__(self, timer_unit="s"):
        self.timer_unit = timer_unit

    def __call__(self, fun):
        @wraps(fun)
        def wrapper(*args, **kwargs):

            print("args: ", args)
            time_str = time.time()

            print(fun.__name__, ": start")
            res = fun(*args, **kwargs)

            time_cost = time.time() - time_str

            unit = self.timer_unit
            if unit == "ms":
                time_cost = time_cost * 1000
            elif unit == "min":
                time_cost = time_cost / 60
            elif unit == "h":
                time_cost = time_cost / 3600
            else:
                unit = "s"

            print(fun.__name__ + " cost: %.3f " % time_cost + unit)
            return res

        return wrapper


@ObjectDecoratorTimer("ms")
def foo(a, b, c):
    # print("foo")
    print(a, b, c)
    time.sleep(0.5)


if __name__ == '__main__':
    foo(3, 54, 6)
    print(foo.__name__)
