class ListaJednokierunkowa:
    class Element:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = self.Element("head")

    def getLastElement(self, head):
        element = head
        if element.next is None:
            return element
        lastelement = element.next
        return self.getLastElement(lastelement)

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
        lastelement = self.getLastElement(self.head)
        lastelement.next = newelement

    def add(self, value, index):
        if index < 0:
            return None
        newelement = self.Element(value)
        newelement.next = self.getElementWithIndex(index)
        previouselement = self.getElementWithIndex(index - 1)
        if previouselement is None and index == 0:
            self.head.next = newelement
            return
        elif previouselement is None:
            print("Indeks dodanego elementu jest zbyt wysoki")
            return
        previouselement.next = newelement

    def remove(self, index):
        if index < 0:
            return None
        element = self.getElementWithIndex(index)
        if index != 0 and self.getElementWithIndex(index) is None:
            print("Indeks elementu jest zbyt wysoki")
            return
        elif index == 0 and element.next is None:
            self.head.next = None
            return
        elif index == 0:
            self.head.next = element.next
            return
        elif element.next is None:
            self.getElementWithIndex(index - 1).next = None
            return
        self.getElementWithIndex(index - 1).next = self.getElementWithIndex(index + 1)

    def find(self, value):
        i = 0
        element = self.head
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
            if element.next is None:
                print(str(index) + ": " + str(element.value) + ", next: " + str(element.next))
            else:
                print(str(index) + ": " + str(element.value) + ", next: " + str(element.next.value))
            element = element.next
            index += 1
            if element is None:
                break
