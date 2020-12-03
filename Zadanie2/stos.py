class Stos:

    def __init__(self, size):
        self.stack = [0] * size
        self.top = -1

    def push(self, value):
        if self.top < (len(self.stack) - 1):
            self.top += 1
            self.stack[self.top] = value
        else:
            print("Stos jest pełny")

    def pop(self):
        value = self.stack[self.top]
        self.top -= 1
        return value

    def find(self, value):
        for i in range(0, len(self.stack)):
            if value == self.stack[i]:
                return i
