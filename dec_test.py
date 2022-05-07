def funA(fun):
    def wrapper():
        print("funA start: ", fun.__name__)
        return fun()

    return wrapper


@funA
def funB():
    print("funB")


if __name__ == '__main__':
    funB()
