class ListaWartownik:
    class Element:
        def __init__(self, value):
            self.value = value
            self.next = None
            self.previous = None

    def __init__(self):
        self.head = self.Element("head")
        self.sentry = self.Element(None)
        self.sentry.previous = self.head
        self.sentry.next = self.head
        self.head.next = self.sentry
        self.tail = self.sentry

    def getElementWithIndex(self, index):
        if index < 0:
            return None
        element = self.sentry.next
        i = 0
        while i < index:
            if element.next is None:
                return None
            element = element.next
            i += 1
        return element

    def addLastElement(self, value):
        newelement = self.Element(value)
        if self.tail == self.sentry:
            newelement.previous = self.sentry
            newelement.next = self.sentry
        else:
            newelement.previous = self.tail
            newelement.next = self.head.next
            self.head.next.previous = newelement
        self.tail.next = newelement
        self.tail = newelement

    def add(self, value, index):
        if index < 0:
            return
        newelement = self.Element(value)
        nextelement = self.getElementWithIndex(index)
        if nextelement is self.sentry:
            self.addLastElement(value)
            return
        newelement.next = nextelement
        previouselement = nextelement.previous
        if previouselement is None and nextelement is self.head:
            self.addLastElement(value)
            return
        elif nextelement == self.head.next and index == 0:
            self.head.next = newelement
            nextelement.previous = newelement
        elif nextelement == self.head.next:
            self.tail = newelement
            nextelement.previous = self.tail
        else:
            nextelement.previous = newelement
        previouselement.next = newelement
        newelement.previous = previouselement

    def remove(self, index):
        if index < 0:
            return
        element = self.getElementWithIndex(index)
        if element.next is element:
            self.head.next = self.head
            self.tail = self.head
            return
        element.previous.next = element.next
        element.next.previous = element.previous
        if element == self.head.next:
            self.head.next = element.next
        if element.next == self.head.next:
            self.tail = element.previous

    def find(self, value):
        i = 0
        element = self.sentry.next
        self.sentry.value = value
        while 1 == 1:
            if element.value == value:
                if element == self.sentry:
                    return None
                else:
                    return i
            element = element.next
            i += 1

    def printList(self):
        element = self.sentry.next
        index = 0
        if element == self.head:
            return None
        while 1 == 1:
            if element.previous == self.sentry and element.next == self.sentry:
                print(
                    str(index) + ": " + str(element.value) + ", next: " + str(element.next.next.value) + ", previous: "
                    + str(self.tail.value))
            elif element.previous == self.sentry:
                print(str(index) + ": " + str(element.value) + ", next: " + str(element.next.value) + ", previous: "
                      + str(self.tail.value))
            elif element.next == self.sentry:
                print(
                    str(index) + ": " + str(element.value) + ", next: " + str(element.next.next.value) + ", previous: "
                    + str(element.previous.value))
            else:
                print(str(index) + ": " + str(element.value) + ", next: " + str(element.next.value) + ", previous: "
                      + str(element.previous.value))
            element = element.next
            index += 1
            if element == self.sentry:
                break
