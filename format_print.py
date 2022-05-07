num = 443.545

print(f"{num}")

print(f'{23.353:08.2f}')

z = 1
x = y = z + 1

d = [] and 56

c = not [1]


class A:
    def __init__(self):
        self.val = 3
        self._val = 56
        self.__val = 78
        self.count = 0
        print("ffff", self.dd)
    dd = 56
    print("fdfd", dd)

    @staticmethod
    def sf():
        print(A.__name__)
        print(A.dd)


    @classmethod
    def cf(cls):
        pass


a = A()
print(a.val)
print(a._val)
print(a._A__val)

A.sf()

class B(A):
    pass