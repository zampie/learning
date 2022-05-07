class A:
    count = 0

    def __init__(self, val=8):
        super(A, self).__init__()
        self.val = val
        print("init a")

    @classmethod
    def cf(cls):
        cls.count += 1

    @staticmethod
    def sf():
        A.count += 1


class B(A):
    def __init__(self):
        super().__init__(5)

    pass


class C(A):
    pass


a = A()


class X:
    def spam(self):
        print('X.spam')
        super(X, self).spam()


class Y:
    def spam(self):
        print("Y.spam")


class Z(X, Y):
    pass


z = Z()
z.spam()

CONFIG={"KEY": "123"}


class Event(object):
    def __init__(self):
        pass


"{event.__init__.__globals__[CONFIG][KEY]}".format(event=Event())



class E:
    """
    dfdfd

    """
    val = 5
    __val = 65
    def __init__(self):
        self.__s_val = 454

e = E()