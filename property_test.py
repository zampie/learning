class Box:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    @property
    def center(self):
        return self.x + self.w / 2, self.y + self.h


if __name__ == '__main__':
    b1 = Box(0, 0, 3, 4)
