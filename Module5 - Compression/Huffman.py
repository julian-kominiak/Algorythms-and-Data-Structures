translated = {}


class Letter:
    def __init__(self, letter, frequency):
        self.letter = letter
        self.frequency = frequency
        self.code = ""

    def appendCode(self, number):
        self.code = number + self.code

    def updateTranslated(self):
        translated[self.letter] = self.code


class Node:
    def __init__(self, leftChild, rightChild):
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.frequency = leftChild.frequency + rightChild.frequency
        self.leftChild.appendCode("0")
        self.rightChild.appendCode("1")
        self.code = ""

    def appendCode(self, number):
        self.code = number + self.code
        self.leftChild.appendCode(number)
        self.rightChild.appendCode(number)

    def updateTranslated(self):
        self.leftChild.updateTranslated()
        self.rightChild.updateTranslated()


def buildHuffmanTree(alphabet, frequency):
    def Frequency(x):
        return x.frequency

    array = [Letter(alphabet[0], frequency[0])]
    for i in range(1, len(alphabet)):
        array.append(Letter(alphabet[i], frequency[i]))
    array.sort(key=Frequency)

    while len(array) > 2:
        currentNode = Node(array[0], array[1])
        array = array[2:]
        for i in range(len(array)):
            if array[i].frequency >= currentNode.frequency:
                array.insert(i, currentNode)
                break
            if i == len(array) - 1:
                array.append(currentNode)
    root = Node(array[0], array[1])
    return root


def encode(alphabet, frequency):
    translated.clear()
    root = buildHuffmanTree(alphabet, frequency)
    root.updateTranslated()
    print(translated)

    encoded = ""
    for char in alphabet:
        for i in translated.keys():
            if char == i:
                encoded += translated[i]
    print(encoded)


def decode(encoded):
    decoded = ""
    while len(encoded) > 0:
        for i in translated.keys():
            if encoded.startswith(translated[i]):
                encoded = encoded[len(translated[i]):]
                decoded += i
    print(decoded)


encode("BACA", [0.1, 0.3, 0.2, 0.3])
decode("00110111")
