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
        if isinstance(leftChild, list):
            for letter in leftChild:
                letter.appendCode("0")
            self.leftChild = splitList(leftChild)
        else:
            self.leftChild = leftChild
            self.leftChild.appendCode("0")
        if isinstance(rightChild, list):
            for letter in rightChild:
                letter.appendCode("1")
            self.rightChild = splitList(rightChild)
        else:
            self.rightChild = rightChild
            self.rightChild.appendCode("1")
        self.code = ""

    def appendCode(self, number):
        self.code = number + self.code
        self.leftChild.appendCode(number)
        self.rightChild.appendCode(number)

    def updateTranslated(self):
        self.leftChild.updateTranslated()
        self.rightChild.updateTranslated()


def splitList(list):
    def getDifference(o):
        return o[1]

    def countDifference(i):
        leftSum = 0
        rightSum = 0
        for node in list[:i]:
            leftSum += node.frequency
        for node in list[i:]:
            rightSum += node.frequency
        return abs(leftSum - rightSum)

    if len(list) == 2:
        return Node(list[0], list[1])
    differences = []
    for i in range(len(list)):
        differences.append((i, countDifference(i)))
    differences.sort(key=getDifference)
    splitPoint = differences[0][0]

    if len(differences[:splitPoint]) == 1:
        return Node(list[0], list[1:])
    elif len(differences[splitPoint:]) == 1:
        return Node(list[:-1], list[-1])
    else:
        return Node(list[:splitPoint], list[splitPoint:])


def buildShannonTree(alphabet, frequency):
    def Frequency(x):
        return x.frequency

    array = [Letter(alphabet[0], frequency[0])]
    for i in range(1, len(alphabet)):
        array.append(Letter(alphabet[i], frequency[i]))
    array.sort(key=Frequency, reverse=True)
    root = splitList(array)
    return root


def encode(alphabet, frequency):
    translated.clear()
    root = buildShannonTree(alphabet, frequency)
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
decode("11100110")
