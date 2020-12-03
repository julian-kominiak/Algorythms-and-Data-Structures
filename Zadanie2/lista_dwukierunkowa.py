class ListaDwukierunkowa:
    class Element:
        def __init__(self, value):
            self.value = value
            self.next = None
            self.previous = None

    def __init__(self):
        self.head = self.Element("head")
        self.tail = self.head

    def getElementWithIndex(self, index):
        if index < 0:
            return None
        element = self.head.next
        i = 0
        if element is None:
            return None
        while i < index:
            if element.next is None:
                return None
            element = element.next
            i += 1
        return element

    def addLastElement(self, value):
        newelement = self.Element(value)
        if self.tail == self.head:
            newelement.previous = None
        else:
            newelement.previous = self.tail
        self.tail.next = newelement
        self.tail = newelement

    def add(self, value, index):
        if index < 0:
            return None
        newelement = self.Element(value)
        nextelement = self.getElementWithIndex(index)
        newelement.next = nextelement
        previouselement = self.getElementWithIndex(index - 1)
        if previouselement is None and index == 0:
            self.head.next = newelement
            if nextelement is None:
                self.tail = newelement
            else:
                nextelement.previous = newelement
            return
        elif previouselement is None:
            print("Indeks dodanego elementu jest zbyt wysoki")
            return
        previouselement.next = newelement
        newelement.previous = previouselement
        if nextelement is None:
            self.tail = newelement
        else:
            nextelement.previous = newelement

    def remove(self, index):
        if index < 0:
            return None
        element = self.getElementWithIndex(index)
        if index != 0 and self.getElementWithIndex(index) is None:
            print("Indeks elementu jest zbyt wysoki")
            return
        elif index == 0 and element.next is None:
            self.head.next = None
            self.tail = self.head
            return
        elif index == 0:
            self.head.next = element.next
            element.next.previous = None
            return
        elif element.next is None:
            element.previous.next = None
            self.tail = element.previous
            return
        nextelement = element.next
        previouselement = element.previous
        previouselement.next = element.next
        nextelement.previous = element.previous

    def find(self, value):
        i = 0
        element = self.head.next
        while 1 == 1:
            if element.value == value:
                return i
            element = element.next
            if element is None:
                return None
            i += 1

    def printList(self):
        element = self.head.next
        index = 0
        if element is None:
            return
        while 1 == 1:
            if element.next is None and element.previous is None:
                print(str(index) + ": " + str(element.value) + ", next: " + str(element.next) + ", previous: "
                      + str(element.previous))
            elif element.next is None:
                print(str(index) + ": " + str(element.value) + ", next: " + str(element.next) + ", previous: "
                      + str(element.previous.value))
            elif element.previous is None:
                print(str(index) + ": " + str(element.value) + ", next: " + str(element.next.value) + ", previous: "
                      + str(element.previous))
            else:
                print(str(index) + ": " + str(element.value) + ", next: " + str(element.next.value) + ", previous: "
                      + str(element.previous.value))
            element = element.next
            index += 1
            if element is None:
                break
        print("tail: " + str(self.tail.value))
