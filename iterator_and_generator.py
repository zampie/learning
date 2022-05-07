from collections import Iterator, Iterable




def foo():
    for i in range(4):
        yield i

if __name__ == '__main__':
    it = foo()

    print(isinstance(it, Iterator))
    # True
    print(isinstance(it, Iterable))
    # True