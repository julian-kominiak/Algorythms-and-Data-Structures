class KolejkaPrioretytowa:

    def __init__(self, size):
        self.queue = [0] * size
        self.head = 0
        self.tail = 0

    def dequeue(self):
        if self.head != self.tail:
            highestvalue = self.queue[self.head]
            highestvalueindex = self.queue[self.head]

            if self.tail > self.head:
                for i in range(self.head, self.tail):
                    if self.queue[i] > highestvalue:
                        highestvalue = self.queue[i]
                        highestvalueindex = i
            else:
                for i in range(0, len(self.queue)):
                    if self.tail <= i < self.head:
                        continue
                    if self.queue[i] > highestvalue:
                        highestvalue = self.queue[i]
                        highestvalueindex = i

            oldhead = self.queue[self.head]
            self.queue[self.head] = highestvalue
            self.queue[highestvalueindex] = oldhead
            value = self.queue[self.head]
            if self.head < (len(self.queue) - 1):
                self.head += 1
            else:
                self.head = 0
            return value
        else:
            return "Kolejka jest pusta"

    def enqueue(self, value):
        if self.tail < (len(self.queue) - 1):
            if self.head != self.tail + 1:
                self.queue[self.tail] = value
                self.tail += 1
            else:
                print("Kolejka jest pełna")
        else:
            if self.head != 0:
                self.queue[self.tail] = value
                self.tail = 0
            else:
                print("Kolejka jest pełna")

    def find(self, value):
        if self.tail > self.head:
            for i in range(self.head, self.tail):
                if self.queue[i] == value:
                    return i
        else:
            for i in range(0, len(self.queue)):
                if self.tail <= i < self.head:
                    continue
                if self.queue[i] > value:
                    return i
