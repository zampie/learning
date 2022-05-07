steps = []

def move(x, y):
    steps.append(x + '->' + y)
    print(x + '->' + y)

def hanoi(n, A='A', B='B', C='C'):
    if n == 1:
        move(A, C)
    else:
        hanoi(n - 1, A, C, B)
        move(A, C)
        hanoi(n - 1, B, A, C)

if __name__ == '__main__':

    hanoi(5)

